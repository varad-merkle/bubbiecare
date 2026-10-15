# bubbiecare
A recruitment system for healthcare workers

This is my implementation based on the model frontend given for the ramp-up activity.

Testing instructions:
<ol>
    <li>Import the code</li>
    <li>Create a new <code>.env</code> file. Paste the contents of the <code>.env.example</code> file and replace your Azure OpenAI API KEY in OPENAI_SUBSCRIPTION_KEY </li>
    <li>Run <code>uv run uvicorn main:app --port 7000</code> in your terminal. The command will start the backend on port 7000</li>
    <li>Start up the bubbiecare frontend - which runs on port 5173</li>
    <li>You should now be able to test all the endpoints!</li>
</ol>
