# Few-shot Prompt Engineering

We give the model input and the expected output to establish the pattern.

By providing examples, we teach the model what we want to do it and how to format the output.

Instead of describing the process, we rely on examples to continue the desired pattern.

## Intermediate Steps: Few-Shot Patterns in Complex Tasks

The examples don't have to be limited to just output and input. We can include intermediate steps to demonstrate achieving a specific goal. This approach is interesting because it allows the large language model to learn how to apply a series of intermediate steps to reach that desired outcome.

Example:

> Situation: I'm traveling at 60mph, and I noticed the brake lights of the car in front of me turning on.
> 
> 
> Think: I need to slow down before I hit that car, so I take action and press on my foot and on to
> 
> the brake.
> 
> Action: Press foot on brake
> 
> Think: The car isn’t going to stop in time
> 
> Action: Check if the shoulder is wide enought to swerve into
> 
> Think: The shoulder is wide enough
> 
> Action: Swerve into the shoulder
> 
> Situation: XXXX
> 
> Action:
> 

The model will then follow the pattern and think through a set of steps.