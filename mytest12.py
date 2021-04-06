def MassVote(N, Votes):
  maximum_value = max(Votes)
  winner = maximum_value/sum(Votes)
  count = 0
  for i in range(len(Votes)):
      if Votes[i] == maximum_value:
          count += 1
  if winner > 0.5 and count == 1:
      return "majority winner " + str(Votes.index(maximum_value) + 1)
  elif winner < 0.5 and count == 1:
      return "minority winner " + str(Votes.index(maximum_value) + 1)
  else:
      return "no winner"
        
