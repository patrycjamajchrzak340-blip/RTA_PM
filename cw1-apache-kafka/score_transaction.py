def score_transaction(tx):
    score = 0
    rules = []

    if tx['hour'] < 6:
        score += 2
        rules.append('R3')

    if tx['category'] == 'elektronika' and tx['amount'] > 1500:
        score += 2
        rules.append('R2')

    if tx['amount'] > 3000:
        score += 3
        rules.append('R1')
    
    return score, rules

# Test
test_tx = {'tx_id': 'TX999', 'amount': 4500.0, 'category': 'elektronika',
           'timestamp': '2026-04-01T03:15:00'}
print(score_transaction(test_tx))  # powinno dać score >= 5
