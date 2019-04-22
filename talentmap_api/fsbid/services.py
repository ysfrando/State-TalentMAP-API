import requests
import logging

from urllib.parse import urlencode

from django.conf import settings

logger = logging.getLogger(__name__)

API_ROOT = settings.FSBID_API_URL


def user_bids(employee_id, position_id=None):
    '''
    Get bids for a user on a position or all if no position
    '''
    bids = requests.get(f"{API_ROOT}/bids/?employeeId={employee_id}").json()
    return [fsbid_bid_to_talentmap_bid(bid) for bid in bids if bid['cyclePosition']['cp_id'] == int(position_id)] if position_id else map(fsbid_bid_to_talentmap_bid, bids)


def bid_on_position(userId, employeeId, cyclePositionId):
    '''
    Submits a bid on a position
    '''
    return requests.post(f"{API_ROOT}/bids", data={"perdet_seq_num": employeeId, "cp_id": cyclePositionId, "userId": userId})


def remove_bid(employeeId, cyclePositionId):
    '''
    Removes a bid from the users bid list
    '''
    return requests.delete(f"{API_ROOT}/bids?cp_id={cyclePositionId}&perdet_seq_num={employeeId}")


def fsbid_bid_to_talentmap_bid(data):
    return {
      "id": "",
      "bidcycle": data['cycle']['description'],
      "emp_id": data['employee']['perdet_seq_num'],
      "user": "",
      "bid_statistics": [
        {
          "id": "",
          "bidcycle": data['cycle']['description'],
          "total_bids": data['cyclePosition']['totalBidders'],
          "in_grade": data['cyclePosition']['atGradeBidders'],
          "at_skill": data['cyclePosition']['inConeBidders'],
          "in_grade_at_skill": data['cyclePosition']['inBothBidders'],
          "has_handshake_offered": data['cyclePosition']['status'] == 'HS',
          "has_handshake_accepted": data['cyclePosition']['status'] == 'HS'
        }
      ],
      "position": {
        "id": data['cyclePosition']['pos_seq_num'],
        "position_number": data['cyclePosition']['pos_seq_num'],
        "grade": "",
        "skill": "",
        "bureau": "",
        "title": "",
        "create_date": data['submittedDate'],
        "update_date": "",
        "post": {
          "id": "",
          "location": {
            "id": "",
            "country": "",
            "code": "",
            "city": "",
            "state": ""
          }
        }
      }
    }

def get_projected_vacancies(query):
  projected_vacancies = requests.get(f"{API_ROOT}/projectedVacancies?{convert_pv_query(query)}").json()
  return  map(fsbid_pv_to_talentmap_pv, projected_vacancies)

def convert_pv_query(query):
  values = {
    "bsn_id": query.get("is_available_in_bidseason"),
    "bureauCode": query.get("bureau__code__in"),
    "dangerPay": query.get("post__danger_pay__in"),
    "gradeCode": query.get("grade__code__in"),
    "languageCode": query.get("language_codes"),
    # "organizationCode": "",
    # "positionNumber": "",
    "postDifferential": query.get("post__differential_rate__in"),
    "skillCode": query.get("skill__code__in"),
    "tourOfDutyCode": query.get("post__tour_of_duty__code__in")
  }
  return urlencode({i:j for i,j in values.items() if j is not None})

def fsbid_pv_to_talentmap_pv(pv):
  return {
    "id": pv["pos_id"],
    "grade": pv["grade"],
    "skill": pv["skill"],
    "bureau": pv["bureau"],
    "organization": pv["organization"],
    "tour_of_duty": pv["tour_of_duty"],
    "languages": [
      {
        "language": pv["language1"],
        "reading_proficiency": pv["reading_proficiency_1"],
        "spoken_proficiency": pv["spoken_proficiency_1"],
        "representation": pv["language_representation_1"]
      }
    ],
    "post": {
      "tour_of_duty": pv["tour_of_duty"],
      "differential_rate": pv["differential_rate"],
      "danger_pay": pv["danger_pay"],
      "location": {
        "id": 7,
        "country": "United States",
        "code": "171670031",
        "city": "Chicago",
        "state": "IL"
      }
    },
    "current_assignment": {
      "user": pv["incumbent"],
      "estimated_end_date": pv["ted"]
    },
    "position_number": pv["position_number"],
    "posted_date": pv["createDate"],
    "title": pv["title"],
    "availability": {
      "availability": True,
      "reason": ""
    },
    "bid_cycle_statuses": [
      {
        "id": pv["pos_id"],
        "bidcycle": pv["bsn_descr_text"],
        "position": "[D0144910] SPECIAL AGENT (Chicago, IL)",
        "status_code": "OP",
        "status": "Open"
      }
    ],
    "bid_statistics": [
      {
        "id": pv["pos_id"],
        "bidcycle": pv["bsn_descr_text"],
        "total_bids": 0,
        "in_grade": 0,
        "at_skill": 0,
        "in_grade_at_skill": 0,
        "has_handshake_offered": False,
        "has_handshake_accepted": False
      }
    ],
    "latest_bidcycle": {
      "id": 1,
      "name": pv["bsn_descr_text"],
      "cycle_start_date": "2018-08-15T19:17:30.065379Z",
      "cycle_deadline_date": "2019-03-27T00:00:00Z",
      "cycle_end_date": "2019-05-16T00:00:00Z",
      "active": True
    }
  }

def get_bid_seasons(bsn_future_vacancy_ind):
  url = f"{API_ROOT}/bidSeasons?=bsn_future_vacancy_ind={bsn_future_vacancy_ind}" if bsn_future_vacancy_ind else f"{API_ROOT}/bidSeasons" 
  bid_seasons = requests.get(f"{API_ROOT}/bidSeasons").json()
  return map(fsbid_bid_season_to_talentmap_bid_season, bid_seasons)

def fsbid_bid_season_to_talentmap_bid_season(bs):
  return {
    "id": bs["bsn_id"],
    "description": bs["bsn_descr_text"],
    "start_date": bs["bsn_start_date"],
    "end_date": bs["bsn_end_date"],
    "panel_cut_off_date": bs["bsn_panel_cutoff_date"]
  }
