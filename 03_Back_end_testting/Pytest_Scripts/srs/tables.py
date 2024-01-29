'''
This file contains all the tables models in the database
'''

from sqlalchemy import Column, Integer
from Portfolio_API.srs.db import Model
from sqlalchemy import Enum
from sqlalchemy.dialects.mysql import VARCHAR


class FindContactors(Model):
    __tablename__ = "find_contractors"
    Id_Contractors = Column(Integer, primary_key=True)
    Verified_companies = Column(Enum('All companies', 'Only verified', name='verified_companies_enum'))
    Slot_name = Column(VARCHAR(45))
    Developers_location = Column(
        Enum('United States', 'Canada', 'Mexico', 'Kyrgyzstan', 'India', name='developers_location_enum'))
    Job_title = Column(Enum('QA Automation', 'QA Manual', name='job_title_enum'))
    Maximum_hourly_rate = Column(Integer)
    Position_level = Column(Enum('Senior', 'Middle', 'Junior', 'Team Lead', name='position_level_enum'))
    Experience = Column(Enum('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', name='experience_enum'))
    English_level = Column(
        Enum('0 (Begginer)', 'A1 (Elementary)', 'A2 (Pre-Entermediate)', 'B1 (Entermediate)', 'B2 (Upper Intermediate)',
             'C1 (Advanced)', 'C2 (Proficient)', name='english_level_enum'))
    Skills = Column(Enum('SQL', 'MySQL', 'MongoDB', 'Git', 'GitHUB', name='skills_enum'))
    Project_Description = Column(VARCHAR(3000))
