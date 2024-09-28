'''
prices = [100, 80, 60, 70, 60, 75, 85]
op: [1, 1, 1, 2, 1, 4, 6]
'''

def calculate_stock_span(prices):
    stack = []  # to store indices
    spans = []  # to store spans

    for i, price in enumerate(prices):
        span = 1

        while stack and prices[stack[-1]] <= price:
            span += spans[stack.pop()]

        stack.append(i)
        spans.append(span)

    return spans
