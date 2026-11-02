from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        tables = defaultdict(lambda: defaultdict(int))

        for customer, table, food in orders:
            foods.add(food)
            tables[table][food] += 1

        food_list = sorted(foods)
        result = [["Table"] + food_list]

        for table in sorted(tables, key=int):
            row = [table]

            for food in food_list:
                row.append(str(tables[table][food]))

            result.append(row)

        return result