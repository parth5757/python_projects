import itertools
import random

class SeatingArrangement:
    def __init__(self, guests, table_sizes):
        """
        Initialize seating arrangement system.
        
        Args:
            guests (list): List of guest names
            table_sizes (list): List of table capacities
        """
        self.guests = guests
        self.table_sizes = table_sizes
        self.tables = [[] for _ in range(len(table_sizes))]
    
    def generate_arrangement(self):
        """
        Generate a random valid seating arrangement.
        """
        # Shuffle guests
        remaining_guests = self.guests.copy()
        random.shuffle(remaining_guests)
        
        # Assign to tables
        for i, table_size in enumerate(self.table_sizes):
            self.tables[i] = remaining_guests[:table_size]
            remaining_guests = remaining_guests[table_size:]
        
        return self.tables
    
    def optimize_arrangement(self, preferences):
        """
        Optimize seating arrangement based on guest preferences.
        
        Args:
            preferences (dict): Dictionary of guest preferences
        """
        best_arrangement = None
        best_score = float('-inf')
        
        # Try multiple random arrangements
        for _ in range(100):
            arrangement = self.generate_arrangement()
            score = self.calculate_happiness(arrangement, preferences)
            
            if score > best_score:
                best_score = score
                best_arrangement = arrangement
        
        return best_arrangement
    
    def calculate_happiness(self, arrangement, preferences):
        """
        Calculate total happiness score for an arrangement.
        
        Args:
            arrangement (list): Current seating arrangement
            preferences (dict): Guest preferences dictionary
        """
        total_happiness = 0
        
        for table in arrangement:
            for i, guest1 in enumerate(table):
                for guest2 in table[i+1:]:
                    if guest1 in preferences and guest2 in preferences[guest1]:
                        total_happiness += preferences[guest1][guest2]
                    elif guest2 in preferences and guest1 in preferences[guest2]:
                        total_happiness += preferences[guest2][guest1]
        
        return total_happiness

# Example usage
guests = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
table_sizes = [3, 3]  # Two tables of 3 people each

# Create seating arrangement
seating = SeatingArrangement(guests, table_sizes)

# Example preferences (higher number means guests prefer to sit together)
preferences = {
    'Alice': {'Bob': 2, 'Charlie': 1},
    'Bob': {'Alice': 2, 'David': 1},
    'Charlie': {'Alice': 1},
    'David': {'Bob': 1},
    'Eve': {'Frank': 2},
    'Frank': {'Eve': 2}
}

# Generate and optimize arrangement
arrangement = seating.optimize_arrangement(preferences)

print("Optimized seating arrangement:")
for i, table in enumerate(arrangement, 1):
    print(f"Table {i}: {', '.join(table)}")