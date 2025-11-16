"""Base OS Class for Genesis Game
Foundation class for all epoch implementations
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseOS(ABC):
    """Abstract base class for all OS epochs in Genesis game"""
    
    def __init__(self, name: str, year: int):
        """Initialize BaseOS
        
        Args:
            name: OS name
            year: Epoch year
        """
        self.name = name
        self.year = year
        self.resources = {
            "cpu": 0,
            "memory": 0,
            "storage": 0,
            "innovation": 0
        }
        self.progression = {
            "current_level": 0,
            "tasks_completed": 0,
            "puzzles_solved": 0,
            "total_points": 0
        }
        self.features = []
        self.is_active = False
    
    @abstractmethod
    def initialize_display(self):
        """Initialize the GUI display for this epoch"""
        pass
    
    @abstractmethod
    def update_display(self):
        """Update the display with current game state"""
        pass
    
    @abstractmethod
    def handle_input(self, action: str):
        """Handle user input/actions
        
        Args:
            action: User action command
        """
        pass
    
    def add_resource(self, resource_type: str, amount: int):
        """Add resources to the OS
        
        Args:
            resource_type: Type of resource (cpu, memory, storage, innovation)
            amount: Amount to add
        """
        if resource_type in self.resources:
            self.resources[resource_type] += amount
    
    def add_feature(self, feature_name: str):
        """Add a new feature to the OS
        
        Args:
            feature_name: Name of the feature
        """
        if feature_name not in self.features:
            self.features.append(feature_name)
    
    def complete_task(self, points: int = 10):
        """Mark a task as complete
        
        Args:
            points: Points earned for task
        """
        self.progression["tasks_completed"] += 1
        self.progression["total_points"] += points
    
    def solve_puzzle(self, points: int = 25):
        """Mark a puzzle as solved
        
        Args:
            points: Points earned for puzzle
        """
        self.progression["puzzles_solved"] += 1
        self.progression["total_points"] += points
    
    def get_status(self) -> Dict[str, Any]:
        """Get current status of the OS
        
        Returns:
            Dictionary containing current status
        """
        return {
            "name": self.name,
            "year": self.year,
            "resources": self.resources.copy(),
            "progression": self.progression.copy(),
            "features": self.features.copy(),
            "is_active": self.is_active
        }
    
    def is_ready_for_next_epoch(self) -> bool:
        """Check if OS is ready to progress to next epoch
        
        Returns:
            True if ready, False otherwise
        """
        return (self.progression["tasks_completed"] >= 5 and 
                self.progression["puzzles_solved"] >= 3)
    
    def __repr__(self) -> str:
        return f"OS({self.name}, {self.year}, Level: {self.progression['current_level']})"
