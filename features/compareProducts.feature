Feature: in order to decide which product has the best quality reported to price
We need an app to create this report

#tech issues
#find the data
#parse the data
#compute the points to have a significant information eg price: 2000 and 5000 can have: (direct: 1,2) , (/500: 4,10) , (/1000:2,5);
#same for shifters: put the position found in my list or add positions from official lists? sh1 , sh2 can have (1,2) or (3, 5)
#make the points to be cumulable.

@wip
  Scenario: Products differ by 1 quality
    Given quality "a"
      | a  | avalue |
      | a1 | 1      |
      | a2 | 2      |
      | b1 | 1      |
      | b2 | 2      |
    And "product" with "aquality" and "bquality"
      | product | aquality | bquality |
      | p4      | a2       | b2       |
      | p3      | a1       | b2       |
      | p2      | a2       | b1       |
      | p1      | a1       | b1       |
    When I compare

    Then i get "products" sorted desc by "score" (sum of values of qualities)

      | products | score |
      | p1       | 2     |
      | p2       | 3     |
      | p3       | 3     |
      | p4       | 4     |


