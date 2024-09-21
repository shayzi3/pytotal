
from dataclasses import dataclass



@dataclass
class GetFile:
     md5: str
     results: dict
     date: int
     size: int
     sandbox_verdict: str | None = None
     status: str | None = None
     
     
     
@dataclass
class GetDomain:
     results: dict
     creation_date: int
     whois: str
     analysis_stats: dict
     
     
     
@dataclass
class RescaneDomain:
     results: dict
     stats: dict
     date: int
     
