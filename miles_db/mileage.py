import sqlite3

db_url = 'mileage.db'   # Assumes the table miles have already been created.

def add_miles(vehicle, new_miles):
    '''If the vehicle is in the database, increment the number of miles by new_miles
    If the vehicle is not in the database, add the vehicle and set the number of miles to new_miles

    If the vehicle is None or new_miles is not a positive number, raise Error
    '''

    if not vehicle:
        raise Exception('Provide a vehicle name')
    if isinstance(new_miles, float) or new_miles < 0:
        raise Exception('Provide a positive number for new miles')

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    rows_mod = cursor.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle))
    if rows_mod.rowcount == 0:
        cursor.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle, new_miles))
    conn.commit()
    conn.close()

def search_vehicle(vehicle):
    '''search vehicle in the database and return its current mileage. If the vehicle
    doesn't exist, return None'''
    conn = sqlite3.connect(db_url)
    cur = conn.cursor()
    sql_statement = ('SELECT * FROM MILES WHERE vehicle = ?')
    search = cur.execute(sql_statement, (vehicle,))
    if search.rowcount == 0:
        return
    else:
        for r in search:
            return r[1]

def change_to_uppercase(vehicle):
    return vehicle.upper()


def main():
    while True:
        try:
            vehicle = input('Enter vehicle name or enter q to quit: ')
            if vehicle == 'q':
                print('Thanks.')
                break
            miles = int(input('Enter new miles for %s: ' % vehicle)) ## TODO input validation
            vehicle = change_to_uppercase(vehicle)
            add_miles(vehicle, miles)
        except ValueError:
            print('New miles must be numerical.')
            miles = int(input('Enter new miles for %s: ' % vehicle))
        vehicle1 = input('Enter vehicle to search: ')
        miles = search_vehicle(vehicle1)
        print(miles)


if __name__ == '__main__':
    main()
