# Operation Exodus - Sebastián Barrios (Cabify)

Last Edited: November 4, 2019 9:44 AM
Tags: cloud, infrastructure, migration, scalability, sre
Created By: Álvaro Bautista Pino

- Migrate from SoftLayer (cloud) to GCP
- Built a migration plan: massive checklist, exhaustively reviewed, running through all different possible scenarios.
- Migration had to be done with no downtime
- Started by accessing data from within old provider
    - **!** redis is not designed to be used across the internet, it is not secure, it is thought to be used within the same network. Connected via tunnel.
    - nsq was synchronized via nsq-synchronizer
- Progressively migrated traffic, caches needed to be populated for the system to be available in the end. All traffic supported from DBs would not work.
- Progress tracked via dashboards
    - Services/Instances are tagged
- Services are organized in tiers:
    - Tier 1 is what you need to complete a ride.
    - Credit card charging is not Tier 1, cause it can be done later. Charging a credit card 6 hours after the ride is not a good experience but it is assumable.
- Testing is done by simulating rides, drivers, customers...
    - Done either manually or automatically by QA Team
- Tackled by the team: infrastructure team along with ambassadors from every other team.