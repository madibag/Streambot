echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/madibag/Streambot /StreamBot
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/madibag/Streambot -b $BRANCH /StreamBot
fi
cd /StreamBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
