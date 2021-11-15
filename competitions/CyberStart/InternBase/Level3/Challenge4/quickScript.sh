
value1=$(curl -s https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D)
value2=$(curl -s https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D)
value3=$(curl -s https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D)
value4=$(curl -s https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D)
value5=$(curl -s https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D)
finValString="$value1""$value2""$value3""$value4""$value5"

echo $finValString