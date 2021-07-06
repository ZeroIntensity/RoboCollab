-- Get an rc_id via the collab name and guild id.
SELECT rc_id FROM collab_data WHERE collab_name = {collab_name} AND dc_id = {dc_id};