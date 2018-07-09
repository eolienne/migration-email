# migration-email

*Purpose* To prepare data for a large email campaign. 

*Goal* 1 row per user. Each website should be listed in its own column so that it can be its own data point upon mailchimp import. 

Source data: 
* List of site owners and their sites on prod (on OR: master project)
* List of sites on prod with vhosts (on OR: all vhosts)
* List of site owners and their sites on dev (on OR: sites dev)
* List of sites on dev with vhosts (on OR: dev vhost)

Flow
1. Acquire above data from developer 
2. Import data sources as separate projects into OpenRefine
3. Use list of site owners and their sites on prod as base (master project) 
4. Run JSON recipe in OpenRefine: migration-email/ortransform.json
5. Export as CSV and open in Excel
6. Delete all columns except "sd_owner","prod_url", and "dev_url"
7. Confirm that column order is as listed in step 6
8. Run python3 transform.py >> output.csv
9. Run python3 transform-dev.py >> output-dev.csv
10. Import output files into mailchimp mailing list separately 
11. Don't forget to update contacts when doing the second import or else _all is lost_
12. Check data in Campaign preview

Current room for improvement as of 9 July 2018, 10:51AM
* Manual deleting of blank cells on output-dev.csv in Excel
* Migrating all work from OpenRefine to Python (steps 2-7)
* Figure out how to transform dev and prod data in the same script
