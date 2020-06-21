def find_cost_of_tile(width, height, cost):
    '''
        Calculate the total cost of tile it would take 
        to cover a floor plan of width and height, using a 
        cost entered by the user.
    '''
    s = int(width * height)
    return s * cost

if __name__ == "__main__":
    one_tile_cost = int(input('please enter the cost of one tile: '))
    price = find_cost_of_tile(10.2, 6.3, 5)
    print(price)
