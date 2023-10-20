# --coding:utf-8--
from aomaker import aomaker


@aomaker.dataclass
class CreatePlan:
    name: str
    env: list
    case_list: list
    project_id: int
    priority: str = "P0"
    cron: str = "* 23 * * *"
    ordered: bool = True
    pass_rate: int = 100
