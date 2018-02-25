# Two dicts:
# 1) file_structure: provides column names for raw csv files
# 2) file_dtypes: provides MYSQL data types for table creation

file_structure = {
    '1': [                      ##      Race file (1 record per race)
                                ##      FILE #1: RACE FILE (1 record per race):
        'track_code',           ##      1       CHARACTER                       3
        'date',                 ##      2       NUMERIC         YYYYMMDD        8
        'race_num',             ##      3       NUMERIC                         2
        'day_evening_flag',     ##      4       CHARACTER                       1       D- Day racing
                                ##                                                      E- Evening racing
        'distance',             ##      5       NUMERIC         99999.99                Most commonly  reported in yds
                                ##                                                      e.g., 1320 for 6 furlongs
        'distance_units',       ##      6       CHARACTER                       1       Y- Yards
                                ##                                                      M- Meters
                                ##                                                      F- Furlongs
        'about_dist_flag',      ##      7       CHARACTER                       1       A- About
                                ##      Three surface related fields are provided for your convenience.
                                ##      Depending on your preference, use whichever field(s) best suits your needs.
                                ##      Field#8 uses the same surface code ('D') for both Dirt and All-Weather surfaces.
                                ##      Field#9 uses a different surface code ('A') for All-Weather surfaces.
                                ##      Field#11 is a flag indicating whether the race was run on an All-Weather surface.

                                ##      Surface, older style
        'surface_old_style',    ##      8       CHARACTER                       1       D- dirt or all weather
                                ##                                                      d- inner dirt
                                ##                                                      T- Main turf
                                ##                                                      t- inner turf
        'surface_new_style',    ##      9       CHARACTER                       1       A- Main All-weather (exclues dirt)
                                ##                                                      D- Main dirft (excludes all weather)
                                ##                                                      d- inner dirt
                                ##                                                      T- Turf
                                ##                                                      t- inner turf
        'reserved10',           ##      10
        'all_weather_flag',     ##      11      CHARACTER                       1       A- All weather surface
        'chute_start_flag',     ##      12      CHARACTER                       1       C- Chute start
        'BRIS_race_type',       ##      13      CHARACTER                       2       G1- Grade I stk/hcp
                                ##                                                      G2- Grade II stk/hcp
                                ##                                                      G3- Grade III  stk/hcp
                                ##                                                      1C- Grade I Canadian
                                ##                                                      2C- Grade II Canadian
                                ##                                                      3C- Grade III Canadian
                                ##                                                      N- Non-graded stk/hcp
                                ##                                                      A- Allowance
                                ##                                                      AO- Allowance Opt. Clmg
                                ##                                                      R- Starter Alw
                                ##                                                      T- Starter Hcp
                                ##                                                      F- Trial
                                ##                                                      C- Claiming
                                ##                                                      CO- Optional Claiming
                                ##                                                      S- Maiden Sp Wt
                                ##                                                      M- Maiden Claiming
                                ##                                                      MO- Maiden Opt. Clmg
                                ##                                                      NO- Optional Clmg Stk
        'equibase_race_type',   ##      14      CHARACTER                       5       CLM- Claiming
                                ##                                                      ALW- Allowance
                                ##                                                      MCL- Maiden Claiming
                                ##                                                      MSW- Maiden Sp Weight
                                ##                                                      STK- Stakes
                                ##                                                      MDN- Maiden
                                ##                                                      STR- Starter Allowance
                                ##                                                      FTR- Futurity Trial
                                ##                                                      AOC- Allowance Opt. Clmg
                                ##                                                      HCP- Handicap
                                ##                                                      SHP- Starter Handicap
                                ##                                                      TRL- Trial
                                ##                                                      etc.
        'race_grade',           ##      15      NUMERIC                         1       0= not graded
                                ##                                                      1= Grade I
                                ##                                                      2= Grade II
                                ##                                                      3= Grade III
                                ##                                                      5= Grade I Canada
                                ##                                                      6= Grade II Canada
                                ##                                                      7= Grade III Canada
        'age_sex_restrictions', ##      16      CHARACTER                       3
                                ##      1st character             2nd character          3rd character
                                ##      -------------             -------------          -------------
                                ##      A - 2 year olds           O - That age only     N -No Sex Restrictions
                                ##      B - 3 year olds           U - That age and up   M -Mares and Fillies Only
                                ##      C - 4 year olds                                 C -Colts and/or Geldings Only
                                ##      D - 5 year olds                                 F -Fillies Only
                                ##      E - 3 & 4 year olds
                                ##      F - 4 & 5 year olds
                                ##      G - 3, 4, & 5 year olds
                                ##      H - all ages
                                ##      Example: 'BON' - means a '3 year olds only' race with no sex restrictions
        'race_restrict_code',   ##      17      CHARACTER                       20      eg.: NW2L, NW29M, NW1Y+, etc.
        'state_bred_flag',      ##      18      CHARACTER                       1       's' - statebred
        'abbrev_race_class',    ##      19      CHARACTER                       20      eg. ALW44000NW2L
        'breed_of_race',        ##      20      CHARACTER                       2       Breed type of race
                                ##                                                      eg. 'TB' for thoroughbred
                                ##      Country code of race
        'country_code',         ##      21      CHARACTER                       3       eg. 'USA'
        'purse',                ##      22      NUMERIC                         8       US dollars
        'total_race_value',     ##      23      NUMERIC                         8       US dollars
        'reserved24',           ##      24
        'reserved25',           ##      25
        'reserved26',           ##      26
        'reserved27',           ##      27
        'max_claim_price',      ##      28      NUMERIC                         7       Highest permitted claiming price of race
        'reserved29',           ##      29
        'race_conditions_1',    ##      30      CHARACTER                       255
        'race_conditions_2',    ##      31      CHARACTER                       255
        'race_conditions_3',    ##      32      CHARACTER                       255
        'race_conditions_4',    ##      33      CHARACTER                       255
        'race_conditions_5',    ##      34      CHARACTER                       255
        'reserved35',           ##      35
        'reserved36',           ##      36
        'field_size',           ##      37      NUMERIC                         2
        'track_condition',      ##      38      CHARACTER                       2       FT- Fast
                                ##                                                      WF- Wet fast
                                ##                                                      FR- FRozen
                                ##                                                      GD- Good
                                ##                                                      SY- Sloppy
                                ##                                                      MY- Muddy
                                ##                                                      SL- Slow
                                ##                                                      HY- Heavy
                                ##                                                      HD- Hard
                                ##                                                      FM- Firm
                                ##                                                      YL- Yielding
                                ##                                                      SF- Soft
                                ##                                                      Etc.
        'fraction_1_time',  ##      39      NUMERIC                 999.99  5.2     [Seconds and hundreths?]
        'fraction_2_time',  ##      40      NUMERIC                 999.99  5.2
        'fraction_3_time',  ##      41      NUMERIC                 999.99  5.2
        'fraction_4_time',  ##      42      NUMERIC                 999.99  5.2
        'fraction_5_time',  ##      43      NUMERIC                 999.99  5.2
        'final_time',       ##      44      NUMERIC                 999.99  5.2
        'fraction_1_dist',  ##      45      NUMERIC                         4       In yards that the fraction time was taken from
        'fraction_2_dist',  ##      46      NUMERIC                         4
        'fraction_3_dist',  ##      47      NUMERIC                         4
        'fraction_4_dist',  ##      48      NUMERIC                         4
        'fraction_5_dist',  ##      49      NUMERIC                         4

        'off_time',         ##      50      CHARACTER                       5       E.g., '00131' for 1:31
                            ##                                                      Depending on the distance of a race, there are up to 6 chart
                            ##                                                      calls reported: start call, point of call 1, 2, 3, Stretch
                            ##                                                      stretch call, and finish call.
                            ##                                                      Point of call 1, 2, and 3 DO NOT necessarily correspond to
                            ##                                                      fraction 1, 2, or 3. The actual distance of any reported
                            ##                                                      fraction and the distance of any reported 'call' is provided
                            ##                                                      in fields 45-49, and 51-54, respectively

        'start_call_dist',  ##      51      NUMERIC                         4       normally reported in yards; 0 for sprints
        'call_dist_first',  ##      52      NUMERIC                         4
        'call_dist_second', ##      53      NUMERIC                         4
        'call_dist_third',  ##      54      NUMERIC                         4

        'race_name',            ##      55      CHARACTER                       80      e.g. 'Kentucky Derby'
        'start_description',    ##      56      CHARACTER                       50
        'temp_rail_dist',       ##      57      NUMERIC                         3       Reported in feet
        'off_turf_flag',        ##      58      CHARACTER                       1       O- Originally scheduled for turf
        'off_turf_dist_change', ##      59      CHARACTER                       1       Y- Distance change
                                ##                                                      N- No distance change
        'reserved60',           ##      60
        'reserved61',           ##      61
        'reserved62',           ##      62
        'weather',              ##      63      CHARACTER                       65
        'race_temp',            ##      64      NUMERIC                         3
        'WPS_show_pool',        ##      65      NUMERIC                         9
        'run_up_dist',          ##      66      NUMERIC                         4
        'reserved67',           ##      67
        'reserved68',           ##      68
        'reserved69',           ##      69
        'reserved70',           ##      70
        'reserved71',           ##      71
        'reserved72',           ##      72
        'reserved73',           ##      73
        'reserved74',           ##      74
        'reserved75',           ##      75
        'reserved76',           ##      76
        'reserved77',           ##      77
        'reserved78',           ##      78
        'reserved79',           ##      79
        'reserved80',           ##      80
        'reserved81',           ##      81
        'reserved82',           ##      82
        'reserved83',           ##      83
        'reserved84',           ##      84
        'reserved85',           ##      85
        'reserved86',           ##      86
        'reserved87',           ##      87
        'reserved88',           ##      88
        'reserved89',           ##      89
        'reserved90',           ##      90
        'reserved91',           ##      91
        'reserved92',           ##      92
        'reserved93',           ##      93
        'reserved94',           ##      94
        'reserved95',           ##      95
        'reserved96',           ##      96
        'reserved97',           ##      97
        'reserved98',           ##      98
        'reserved99'            ##      99
    ],

    '2': [                      ##      Start file (1 record per start)
        'track_code',           ##      1       CHARACTER                       3
        'date',                 ##      2                       YYYYMMDD        8
        'race_num',             ##      3       NUMERIC                         1
        'day_evening_flag',     ##      4       CHARACTER                       1       D- Day racing
                                ##                                                      E- Evening racing
        'horse_name',           ##      5       CHARACTER                       25
        'foreign_bred_code',    ##      6       CHARACTER                       5       Country code if foreign bred (non-US, CAN, PR)
        'state_bred_code',      ##      7       CHARACTER                       5       Statebred code if US,CAN,or PR bred
        'post_position',        ##      8       CHARACTER                       2       May contain 99 if scratched
        'program_number',       ##      9       CHARACTER                       3       May also contain coupled letter
                                ##                                                      '1A' or 'SCR' if scratched
        'birth_year',           ##      10      NUMERIC         CCYY            4
        'breed',                ##      11      CHARACTER                       2
        'coupled_flag',         ##      12      CHARACTER                       1       When applicable, this field will
                                ##                                                      usually contain the coupled letter
                                ##                                                      (A,B,C,D,E,F,X,Y,...)
        'jockey_name',          ##      13      CHARACTER                       25      Abbreviated
        'jockey_last_name',     ##      14      CHARACTER                       25
        'jockey_first_name',    ##      15      CHARACTER                       15
        'jockey_middle_name',   ##      16      CHARACTER                       15
        'reserved17',           ##      17
        'trainer_name',         ##      18      CHARACTER                       30      Abbreviated
        'trainer_last_name',    ##      19      CHARACTER                       80
        'trainer_first_name',   ##      20      CHARACTER                       15
        'trainer_middle_name',  ##      21      CHARACTER                       15
        'trip_comment',         ##      22      CHARACTER                       22
        'reserved23',           ##      23
        'owner_name',           ##      24      CHARACTER                       80
        'owner_first_name',     ##      25      CHARACTER                       15      First & middle owner name is
        'owner_middle_name',    ##      26      CHARACTER                       15      sometimes provided when there
                                ##                                                      is only a single owner
        'claiming_price',       ##      27      NUMERIC                         8       Claiming Price of the HORSE
        'medication_codes',     ##      28      CHARACTER                       7       A- Adjunct Bleeder Medication
                                ##                                                      B- Bute
                                ##                                                      C- First time Bute
                                ##                                                      L- Lasix
                                ##                                                      M- First Lasix
                                ##                                                      eg. 'BM' for Bute, First lasix
        'equipment_code',       ##      29      CHARACTER                       7       No Equipment
                                ##                                                      1 Running W's
                                ##                                                      2 Screens
                                ##                                                      3 Shields
                                ##                                                      A Aluminum Pads
                                ##                                                      B Blinkers
                                ##                                                      C Mud Calks
                                ##                                                      D Glued Shoes
                                ##                                                      E Inner Rims
                                ##                                                      F Front bandages
                                ##                                                      G Goggles
                                ##                                                      H Outer Rims
                                ##                                                      I Inserts
                                ##                                                      J Aluminum Pad
                                ##                                                      K Flipping halter
                                ##                                                      L Bar Shoes
                                ##                                                      M Blocks
                                ##                                                      N No Whip
                                ##                                                      O Blinkers Off
                                ##                                                      P Pads
                                ##                                                      Q Nasal Strip off
                                ##                                                      R Bar Shoe
                                ##                                                      S Nasal Strip
                                ##                                                      T Turndowns
                                ##                                                      U Spurs
                                ##                                                      W Queen's Plates
                                ##                                                      Y No shoes
                                ##                                                      Z Tongue tie
        'earnings',             ##      30      NUMERIC                         9       US Dollars
        'odds',                 ##      31      NUMERIC         9999.99         6.2
        'nonbetting_flag',      ##      32      CHARACTER                       1       Y- nonbetting starter
        'favorite_flag',        ##      33      NUMERIC                         1       1- favorite
        'reserved34',           ##      34                                              0- Non-favorite
        'reserved35',           ##      35
        'disqualified_flag',    ##      36      CHARACTER                               Y- Disqualified
        'disqualified_placing', ##      37      NUMERIC                         2       Official placing if Dq'd, otherwise: 0
        'weight',               ##      38      NUMERIC                         4
        'corrected_weight',     ##      39      CHARACTER                       1       Y- if different than program weight
        'overweight_amt',       ##      40      NUMERIC                         3       OW= (Weight carried - Program weight)
        'claimed_flag',         ##      41      CHARACTER                       1       Y- horse was claimed
        'claimed_trainer',      ##      42      CHARACTER                       30      Abbreviated
        'claimed_trainer_last', ##      43      CHARACTER                       25
        'claimed_trainer_first',##      44      CHARACTER                       15
        'claimed_trainer_middle',   ##  45      CHARACTER                       15
        'reserved46',           ##      46
        'claimed_owner',        ##      47      CHARACTER                       40      Abbreviated
        'claimed_owner_last',   ##      48      CHARACTER                       80
        'claimed_owner_first',  ##      49      CHARACTER                       15
        'claimed_owner_middle', ##      50      CHARACTER                       15

        'win_payout',           ##      51      NUMERIC         9999.99         6.2     If any
        'place_payout',         ##      52      NUMERIC         9999.99         6.2     If any
        'show_payout',          ##      53      NUMERIC         9999.99         6.2     If any
        'reserved54',           ##      54

        'start_call_pos',       ##      55      NUMERIC                         2       Position
        '1st_call_pos',         ##      56      NUMERIC                         3
        '2d_call_pos',          ##      57      NUMERIC                         3
        '3d_call_pos',          ##      58      NUMERIC                         3
        'stretch_call_pos',     ##      59      NUMERIC                         3
        'finish_pos',           ##      60      NUMERIC                         3       Original finish position
        'official_finish_pos',  ##      61      NUMERIC                         3       Official finish position

        'start_lead',           ##      62      NUMERIC                         5.2     For leader only
        '1st_call_lead',        ##      63      NUMERIC                         5.2     For leader only
        '2d_call_lead',         ##      64      NUMERIC                         5.2     For leader only
        '3d_call_lead',         ##      65      NUMERIC                         5.2     For leader only
        'stretch_call_lead',         ##      66      NUMERIC                         5.2     For leader only
        'finish_lead',          ##      67      NUMERIC                         5.2     For leader only

        'start_beaten',         ##      68      NUMERIC                         5.2     leader- 0
        '1st_call_beaten',      ##      69      NUMERIC                         5.2
        '2d_call_beaten',       ##      70      NUMERIC                         5.2
        '3d_call_beaten',       ##      71      NUMERIC                         5.2
        'stretch_call_beaten',  ##      72      NUMERIC                         5.2
        'finish_beaten',        ##      73      NUMERIC                         5.2

        'start_margin',         ##      74      NUMERIC                         5.2     Lengths ahead of closest trailing horse
        '1st_call_margin',      ##      75      NUMERIC                         5.2
        '2d_call_margin',       ##      76      NUMERIC                         5.2
        '3d_call_margin',       ##      77      NUMERIC                         5.2
        'stretch_call_margin',  ##      78      NUMERIC                         5.2
        'finish_margin',        ##      79      NUMERIC                         5.2

        'dead_heat_flag',       ##      80      CHARACTER                       2       DH - dead heat

        'horse_reg_id',         ##      81      CHARACTER                       8
        'jockey_id',            ##      82      NUMERIC
        'trainer_id',           ##      83      NUMERIC
        'owner_id',             ##      84      NUMERIC
        'claimed_trainer_id',   ##      85      NUMERIC                                 When applicable
        'claimed_owner_id',     ##      86      NUMERIC                                 When applicable

        'reserved87',           ##      87
        'reserved88',           ##      88
        'reserved89',           ##      89
        'reserved90',           ##      90
        'reserved91',           ##      91
        'reserved92',           ##      92
        'reserved93',           ##      93
        'reserved94',           ##      94
        'reserved95',           ##      95
        'reserved96',           ##      96
        'reserved97',           ##      97
        'reserved98',           ##      98
        'reserved99',           ##      99
    ],

    '3': [                      ##      ITM payoff file
                                ##                                                      1 record for each itm finisher
    'track_code',               ##      1       CHARACTER                       3
    'date',                     ##      2                       YYYYMMDD        8
    'race_num',                 ##      3       NUMERIC                         2
    'day_evening_flag',         ##      4       CHARACTER                       2       D- Day racing
                                ##                                                      E- Evening Racing
    'horse_name',               ##      5       CHARACTER                       25
    'foreign_bred_code',        ##      6       CHARACTER                       5       Country code if foreign bred
    'statebred_code',           ##      7       CHARACTER                       5       Statebred code if domestic bred
    'program_number',           ##      8       CHARACTER                       3

    'win_payout',               ##      9       NUMERIC                         6.2
    'place_payout',             ##      10      NUMERIC                         6.2
    'show_payout',              ##      11      NUMERIC                         6.2

    'reserved12',               ##      12
    'reserved13',               ##      13
    'reserved14',               ##      14
    'reserved15',               ##      15
    'reserved16',               ##      16
    'reserved17',               ##      17
    'reserved18',               ##      18
    'reserved19',               ##      19
    'reserved20',               ##      20
    'reserved21',               ##      21
    'reserved22',               ##      22
    'reserved23',               ##      23
    'reserved24',               ##      24
    'reserved25',               ##      25
    ],

    '4': [                      ##      Exotic Payoff File (1 record for each payoff)
        'track_code',           ##      1       CHARACTER                       3
        'date',                 ##      2                       YYYYMMDD        8
        'race_num',             ##      3       NUMERIC                         2
        'day_evening_flag',     ##      4       CHARACTER                       1       D- Day Racing
        'wager_type',           ##      5       CHARACTER                       45      E- Evening Racing
        'bet_amount',           ##      6       NUMERIC         999.99          5.2
        'payout_amount',        ##      7       NUMERIC         999999999.99    11.2
        'number_correct',       ##      8       NUMERIC                         5       Used for races like Pick6. This field reflects the
                                ##                                                      number correct for this record. There will often
                                ##                                                      be two records for a wager ...one record may show '6'
                                ##                                                      correct (and it's corresponding payoff) and
                                ##                                                      another record may show '5' correct (and it's
                                ##                                                      corresponding payoff).
        'winning_numbers',      ##      9       CHARACTER                       45      may also contain the word 'ALL' and '/' and '-'
        'wager_pool',           ##      10      NUMERIC         999999999.99    11.2
        'carryover_amount',     ##      11      NUMERIC         999999999.99    11.2
        'reserved13',           ##      12
        'reserved14',           ##      13
        'reserved15',           ##      14
        'reserved16',           ##      15
        'reserved17',           ##      16
        'reserved18',           ##      17
        'reserved19',           ##      18
        'reserved20',           ##      19
        'reserved21',           ##      20
        'reserved22',           ##      21
        'reserved23',           ##      22
        'reserved24',           ##      23
        'reserved25',           ##      24
        'reserved26',           ##      25
    ],

    '5': [                      ##      FILE #5: BREEDING File (1 record per race winner)

        'track_code',           ##      1       CHARACTER                       3
        'date',                 ##      2       CHARACTER       YYYYMMDD        8
        'race_num',             ##      3       NUMERIC                         2
        'day_evening_flag',     ##      4       CHARACTER                       1       D- Day Racing
        'horse_name',           ##      5       CHARACTER                       25      E- Evening Racing
        'foreignbred_code',     ##      6       CHARACTER                       5       Country code if foreign bred
        'statebred_code',       ##      7       CHARACTER                       5       Statebred code if domestic bred
        'program_number',       ##      8       CHARACTER                       3
        'breeder',              ##      9       CHARACTER                       80
        'color',                ##      10      CHARACTER                       20
        'foal_date',            ##      11                      YYYYMMDD        8
        'age',                  ##      12      NUMERIC                         2
        'sex',                  ##      13      CHARACTER                       1
        'sire',                 ##      14      CHARACTER                       25
        'dam',                  ##      15      CHARACTER                       25
        'broodmare_sire',       ##      16      CHARACTER                       25
        'reserved17',           ##      17
        'reserved18',           ##      18
        'reserved19',           ##      19
        'reserved20',           ##      20
        'reserved21',           ##      21
        'reserved22',           ##      22
        'reserved23',           ##      23
        'reserved24',           ##      24
        'reserved25',           ##      25
    ],

    '6': [                      ##      FOOTNOTES File (usually contains multiple records per race)
        "track_code",           ##      1       CHARACTER                       3
        "date",                 ##      2                       YYYYMMDD        8
        "race_num",             ##      3       NUMERIC                         2
        "day_evening_flag",     ##      4       CHARACTER                       1       D- Day Racing
        "footnote_sequence",    ##      5       NUMERIC                         2       E- Evening Racing
        "footnote_text",        ##      6       CHARACTER                       80
        "reserved7",            ##      7
        "reserved8",            ##      8
        "reserved9",            ##      9
        "reserved10",            ##      10
    ],

    'DRF': [   ## Up to date as of 4/28/2014
        ## DESCRIPTION                  Field   TYPE            FORMAT          LENGTH  COMMENTS

        ## *** Today's Race Data ***
        'track',                    ##      1       CHARACTER       XXX             3
        'date',                     ##      2       CHARACTER       XXXXXXXX        8
        'race',                     ##      3       NUMERIC         99              2
        'post_position',            ##      4       NUMERIC         99              2
        'entry',                    ##      5       CHARACTER       X               1       A- part of A entry
                                    ##                                                      B- part of B entry
                                    ##                                                      C- part of C entry
                                    ##                                                      F- part of FIELD
                                    ##                                                      S- if scratched
        'distance',                 ##      6       NUMERIC         99999           5       In yards
                                    ##                                                      Negative value for about distances
        'surface',                  ##      7       CHARACTER       X               1       D- dirt
                                    ##                                                      T- turf
                                    ##                                                      d- inner dirt
                                    ##                                                      t- inner turf
                                    ##                                                      s- steeplechase
                                    ##                                                      h- hunt
        'reserved8',                ##      8
        'race_type',                ##      9       CHARACTER       XX              2       G1- Grade I stk/hcp
                                    ##                                                      G2- Grade II stk/hcp
                                    ##                                                      G3- Grade III stk/hcp
                                    ##                                                      N- nongraded stake/handicap
                                    ##                                                      A- allowance
                                    ##                                                      R- Starter Alw
                                    ##                                                      T- Starter Hcp
                                    ##                                                      C- claiming
                                    ##                                                      CO- Optional Clmg
                                    ##                                                      S- mdn sp wt
                                    ##                                                      M- mdn claimer
                                    ##                                                      AO- Alw Opt Clm
                                    ##                                                      MO- Mdn Opt Clm
                                    ##                                                      NO- Opt Clm Stk
        'age_sex_restricts',        ##      10      CHARACTER       XXX                     see codes below
        'today_race_class',         ##      11      CHARACTER       X(14)                   (eg. 'Alw44000n2L') NEED TO PARSE THESE AND CREATE A NEW ITEM
        'purse',                    ##      12      NUMERIC         99999999        8
        'claiming_price',           ##      13      NUMERIC         9999999         7
        'horse_claiming_price',     ##      14      NUMERIC         9999999         7       blank if N.A.
        'track_record_pace',        ##      15      NUMERIC         999.99          6       seconds & hundredths IS THIS FOR TYPE? DISTANCE? WHAT IS THE RECORD BASED ON?
        'race_conditions',          ##      16      CHARACTER                       500     see also field #225-239
        'lasix_list',               ##      17      CHARACTER                       400     (Blank except 1st horse each race)
                                    ##                                                      (see also field #63)
        'bute_list',                ##      18      CHARACTER                       400     '        '
        'coupled_list',             ##      19      CHARACTER                       200     '        '
        'mutuel_list',              ##      20      CHARACTER                       200     '        '
        'simulcast_track_code',     ##      21      CHARACTER       XXX             3       (actual track code if not a
                                    ##                                                      simulcast)
        'simulcast_track_race',     ##      22      NUMERIC         99              2       (actual race # if not a
                                    ##                                                      sumulcast)
        'breed_type',               ##      23      CHARACTER       XX              2       (if available) Some of the
                                    ##                                                      types:
                                    ##                                                      AP-Appaloosa
                                    ##                                                      AR-Arabian
                                    ##                                                      PT-Paint/Pinto
                                    ##                                                      QH-Quarter Horse
                                    ##                                                      TB-Thoroughbred
                                    ##                                                      NB-Non-tbred in TJC registry
        'today_nasal_strip_chg',    ##      24      NUMERIC         9               1       0=No Change
                                    ##                                                      1=Nasal Strip ON
                                    ##                                                      2=Nasal Strip OFF
                                    ##                                                      9=Information Unavailable
        'allweather_surface',       ##      25                      X               1       A- All Weather Surface flag
        'reserved26',               ##      26
        'reserved27',               ##      27

        ##*** Today's Horse/Trainer/Jockey/Owner ***
        'trainer',                  ##      28      CHARACTER                       30
        'trainer_starts',           ##      29      NUMERIC         9999            4       Current meet
        'trainer_wins',             ##      30      NUMERIC         999             3       Current meet
        'trainer_places',           ##      31      NUMERIC         999             3       Current meet
        'trainer_shows',            ##      32      NUMERIC         999             3       Current meet
        'jockey',                   ##      33      CHARACTER                       25
        'apprentice_wgt_alw',       ##      34      NUMERIC         99              2       (if any)
        'jockey_starts',            ##      35      NUMERIC         9999            4       Current meet
        'jockey_wins',              ##      36      NUMERIC         999             3       Current meet
        'jockey_places',            ##      37      NUMERIC         999             3       Current meet
        'jockey_shows',             ##      38      NUMERIC         999             3       Current meet
        'todays_owner',             ##      39      CHARACTER                       40
        'owners_silks',             ##      40      CHARACTER                       100
        'main_track_only_AE',       ##      41      CHARACTER                       1       'M' for MTO
                                    ##                                                      'A' for A.E.
        'reserved42',               ##      42                                              For possible future expansion
        'program_number',           ##      43      CHARACTER       XXX             3
        'morning_line',             ##      44      NUMERIC         999.99          6       (if available)

        ##*** Horse History Data ***
        'horse_name',               ##      45      CHARACTER                       25
        'birth_year',               ##      46      NUMERIC         99              2
        'foaling_month',            ##      47      NUMERIC         99              2       1  for Jan, 12 for Dec
        'reserved48',               ##      48
        'sex',                      ##      49      CHARACTER       X               1
        'color',                    ##      50      CHARACTER                       5
        'weight',                   ##      51      NUMERIC         999             3
        'sire',                     ##      52      CHARACTER                       25
        'sires_sire',               ##      53      CHARACTER                       25
        'dam',                      ##      54      CHARACTER                       25
        'dams_sire',                ##      55      CHARACTER                       25
        'breeder',                  ##      56      CHARACTER                       67
        'where_bred',               ##      57      CHARACTER                       5       Abbreviation
        'program_post_pos',         ##      58                      XX              2       (if available) Updated Post
                                    ##                                                      after early scratches (as
                                    ##                                                      displayed on program)
        'reserved59',               ##      59
        'reserved60',               ##      60
        'reserved61',               ##      61

        ##*** Current Horse Stats ***

        'todays_meds_new',          ##      62      NUMERIC                         2       0=None
                                    ##                                                      1=Lasix, w/1st time Lasix info
                                    ##                                                      2=Bute
                                    ##                                                      3=Bute & Lasix see also
                                    ##                                                      fields #17 & #18
                                    ##                                                      4=1st time Lasix
                                    ##                                                      5=Bute & 1st Lasix
                                    ##                                                      9=Medication info unavailable
        'todays_meds_old',          ##      63      NUMERIC                         1       0=None
                                    ##                                                      1=Lasix, w/o 1st time Lasix
                                    ##                                                      info
                                    ##                                                      2=Bute
                                    ##                                                      3=Bute & Lasix see also fields
                                    ##                                                          17 & #18
                                    ##                                                      9=Medication info unavailable
        'equipment_change',         ##      64      NUMERIC                         1       0=No change
                                    ##                                                      1=Blinkers on
                                    ##                                                      2=Blinkers off
                                    ##                                                      9=Equipment info unavailable

        ##      Horse's Lifetime Record @ Today's Distance

        'life_distance_starts',     ##      65      NUMERIC         999             3
        'life_distance_wins',       ##      66      NUMERIC         99              2
        'life_distance_places',     ##      67      NUMERIC         99              2
        'life_distance_shows',      ##      68      NUMERIC         99              2
        'life_distance_earned',     ##      69      NUMERIC         99999999        8

        ##      Horse's Lifetime Record @ Today's track:

        'life_track_starts',        ##      70      NUMERIC         999             3
        'life_track_wins',          ##      71      NUMERIC         99              2
        'life_track_places',        ##      72      NUMERIC         99              2
        'life_track_shows',         ##      73      NUMERIC         99              2
        'life_track_earned',        ##      74      NUMERIC         99999999        8

        ##      Horse's Lifetime Turf Record:

        'life_turf_starts',         ##      75      NUMERIC         999             3
        'life_turf_wins',           ##      76      NUMERIC         99              2
        'life_turf_places',         ##      77      NUMERIC         99              2
        'life_turf_shows',          ##      78      NUMERIC         99              2
        'life_turf_earned',       ##      79      NUMERIC         99999999        8

        ##      Horse's Lifetime Wet Record:

        'life_wet_starts',          ##      80      NUMERIC         999             3
        'life_wet_wins',            ##      81      NUMERIC         99              2
        'life_wet_places',          ##      82      NUMERIC         99              2
        'life_wet_shows',           ##      83      NUMERIC         99              2
        'life_wet_earned',          ##      84      NUMERIC         99999999        8

        #       Horse's Current Year Record:

        'current_year_year',        ##      85      NUMERIC         9999            4       (eg. 2005)
        'current_year_starts',      ##      86      NUMERIC         99              2
        'current_year_wins',        ##      87      NUMERIC         99              2
        'current_year_places',      ##      88      NUMERIC         99              2
        'current_year_shows',       ##      89      NUMERIC         99              2
        'current_year_earned',      ##      90      NUMERIC         99999999        8

        ##      Horse's Previous Year Record:

        'past_year_year',           ##      91      NUMERIC         9999            4       (eg. 2004)
        'past_year_starts',         ##      92      NUMERIC         99              2
        'past_year_wins',           ##      93      NUMERIC         99              2
        'past_year_places',         ##      94      NUMERIC         99              2
        'past_year_shows',          ##      95      NUMERIC         99              2
        'past_year_earned',         ##      96      NUMERIC         99999999        8

        ##      Horse's Lifetime Record:

        'lifetime_starts',          ##      97      NUMERIC         999             3
        'lifetime_wins',            ##      98      NUMERIC         999             3
        'lifetime_places',          ##      99      NUMERIC         999             3
        'lifetime_shows',           ##      100     NUMERIC         999             3
        'lifetime_earned',          ##      101     NUMERIC         99999999        8

        ##      Recent Workouts

        'workout_date_1',           ##      102     DATE            99999999        8       CYMD
        'workout_date_2',           ##      103     DATE            99999999        8       CYMD
        'workout_date_3',           ##      104     DATE            99999999        8       CYMD
        'workout_date_4',           ##      105     DATE            99999999        8       CYMD
        'workout_date_5',           ##      106     DATE            99999999        8       CYMD
        'workout_date_6',           ##      107     DATE            99999999        8       CYMD
        'workout_date_7',           ##      108     DATE            99999999        8       CYMD
        'workout_date_8',           ##      109     DATE            99999999        8       CYMD
        'workout_date_9',           ##      110     DATE            99999999        8       CYMD
        'workout_date_10',          ##      111     DATE            99999999        8       CYMD
        'workout_date_11',          ##      112     DATE            99999999        8       CYMD
        'workout_date_12',          ##      113     DATE            99999999        8       CYMD

        'workout_time_1',           ##      114     NUMERIC         9999.99         7       seconds & hundredths
                                    ##                                                      Negative time if a
                                    ##                                                      'bullet' work (ie. -34.80
                                    ##                                                      means a bullet work in
                                    ##                                                      a time of 34 4/5)
        'workout_time_2',           ##      115     NUMERIC         9999.99         7
        'workout_time_3',           ##      116     NUMERIC         9999.99         7
        'workout_time_4',           ##      117     NUMERIC         9999.99         7
        'workout_time_5',           ##      118     NUMERIC         9999.99         7
        'workout_time_6',           ##      119     NUMERIC         9999.99         7
        'workout_time_7',           ##      120     NUMERIC         9999.99         7
        'workout_time_8',           ##      121     NUMERIC         9999.99         7
        'workout_time_9',           ##      122     NUMERIC         9999.99         7
        'workout_time_10',          ##      123     NUMERIC         9999.99         7
        'workout_time_11',          ##      124     NUMERIC         9999.99         7
        'workout_time_12',          ##      125     NUMERIC         9999.99         7

        'workout_track_1',          ##      126     CHARACTER                       10
        'workout_track_2',          ##      127     CHARACTER                       10
        'workout_track_3',          ##      128     CHARACTER                       10
        'workout_track_4',          ##      129     CHARACTER                       10
        'workout_track_5',          ##      130     CHARACTER                       10
        'workout_track_6',          ##      131     CHARACTER                       10
        'workout_track_7',          ##      132     CHARACTER                       10
        'workout_track_8',          ##      133     CHARACTER                       10
        'workout_track_9',          ##      134     CHARACTER                       10
        'workout_track_10',         ##      135     CHARACTER                       10
        'workout_track_11',         ##      136     CHARACTER                       10
        'workout_track_12',         ##      137     CHARACTER                       10

        'workout_distance_1',       ##      138     NUMERIC         99999           5       (Dist. in yards)
        'workout_distance_2',       ##      139     NUMERIC         99999           5       (- value for about distances)
        'workout_distance_3',       ##      140     NUMERIC         99999           5
        'workout_distance_4',       ##      141     NUMERIC         99999           5
        'workout_distance_5',       ##      142     NUMERIC         99999           5
        'workout_distance_6',       ##      143     NUMERIC         99999           5
        'workout_distance_7',       ##      144     NUMERIC         99999           5
        'workout_distance_8',       ##      145     NUMERIC         99999           5
        'workout_distance_9',       ##      146     NUMERIC         99999           5
        'workout_distance_10',      ##      147     NUMERIC         99999           5
        'workout_distance_11',      ##      148     NUMERIC         99999           5
        'workout_distance_12',      ##      149     NUMERIC         99999           5

        'workout_condition_1',      ##      150     CHARACTER       XX              2       Track condition
        'workout_condition_2',      ##      151     CHARACTER       XX              2
        'workout_condition_3',      ##      152     CHARACTER       XX              2
        'workout_condition_4',      ##      153     CHARACTER       XX              2
        'workout_condition_5',      ##      154     CHARACTER       XX              2
        'workout_condition_6',      ##      155     CHARACTER       XX              2
        'workout_condition_7',      ##      156     CHARACTER       XX              2
        'workout_condition_8',      ##      157     CHARACTER       XX              2
        'workout_condition_9',      ##      158     CHARACTER       XX              2
        'workout_condition_10',     ##      159     CHARACTER       XX              2
        'workout_condition_11',     ##      160     CHARACTER       XX              2
        'workout_condition_12',     ##      161     CHARACTER       XX              2

        'workout_description_1',    ##      162     CHARACTER       XXX             3       1st Character: H or B
        'workout_description_2',    ##      163     CHARACTER       XXX             3       H for Handily   B for Breezing
        'workout_description_3',    ##      164     CHARACTER       XXX             3
        'workout_description_4',    ##      165     CHARACTER       XXX             3       2nd Character: g
        'workout_description_5',    ##      166     CHARACTER       XXX             3       if worked from gate
        'workout_description_6',    ##      167     CHARACTER       XXX             3
        'workout_description_7',    ##      168     CHARACTER       XXX             3       3rd Character: D
        'workout_description_8',    ##      169     CHARACTER       XXX             3       if 'Dogs are up'
        'workout_description_9',    ##      170     CHARACTER       XXX             3
        'workout_description_10',   ##      171     CHARACTER       XXX             3
        'workout_description_11',   ##      172     CHARACTER       XXX             3
        'workout_description_12',   ##      173     CHARACTER       XXX             3

        'workout_track_type_1',     ##      174     CHARACTER       XX              1[???]  MT-main dirt
        'workout_track_type_2',     ##      175     CHARACTER       XX              1[???]  IM-inner dirt
        'workout_track_type_3',     ##      176     CHARACTER       XX              1[???]  T-main turf
        'workout_track_type_4',     ##      177     CHARACTER       XX              1[???]  IT-inner turf
        'workout_track_type_5',     ##      178     CHARACTER       XX              1[???]  WC-wood chip
        'workout_track_type_6',     ##      179     CHARACTER       XX              1[???]  HC-hillside course
        'workout_track_type_7',     ##      180     CHARACTER       XX              1[???]  TN-trf trn trk
        'workout_track_type_8',     ##      181     CHARACTER       XX              1[???]  IN-inner trf trn track
        'workout_track_type_9',     ##      182     CHARACTER       XX              1[???]  TR-training race
        'workout_track_type_10',    ##      183     CHARACTER       XX              1[???]  --If blank, track type
        'workout_track_type_11',    ##      184     CHARACTER       XX              1[???]  unknown
        'workout_track_type_12',    ##      185     CHARACTER       XX              1[???]

        'same_workouts_all_day_1',  ##      186
        'same_workouts_all_day_2',  ##      187
        'same_workouts_all_day_3',  ##      188
        'same_workouts_all_day_4',  ##      189
        'same_workouts_all_day_5',  ##      190
        'same_workouts_all_day_6',  ##      191
        'same_workouts_all_day_7',  ##      192
        'same_workouts_all_day_8',  ##      193
        'same_workouts_all_day_9',  ##      194
        'same_workouts_all_day_10', ##      195
        'same_workouts_all_day_11', ##      196
        'same_workouts_all_day_12', ##      197

        'rank_same_workout_1',      ##      198                                             among others that day/dist
        'rank_same_workout_2',      ##      199
        'rank_same_workout_3',      ##      200
        'rank_same_workout_4',      ##      201
        'rank_same_workout_5',      ##      202
        'rank_same_workout_6',      ##      203
        'rank_same_workout_7',      ##      204
        'rank_same_workout_8',      ##      205
        'rank_same_workout_9',      ##      206
        'rank_same_workout_10',     ##      207
        'rank_same_workout_11',     ##      208
        'rank_same_workout_12',     ##      209


        'bris_run_style',           ##      210     CHARACTER       XXX             3
        'quirin_speed_points',      ##      211     NUMERIC         9               1

        'reserved212',              ##      212
        'reserved213',              ##      213

        '2f_bris_pace_par',         ##      214     NUMERIC         999             3       for level
        '4f_bris_pace_par',         ##      215     NUMERIC         999             3
        '6f_bris_pace_par',         ##      216     NUMERIC         999             3
        'bris_speed_par',           ##      217     NUMERIC         999             3       for class level
        'bris_late_pace_par',       ##      218     NUMERIC         999             3       for level

        'TJ_starts',                ##      219     NUMERIC         9999            4       365 days
        'TJ_wins',                  ##      220     NUMERIC         9999            4
        'TJ_places',                ##      221     NUMERIC         9999            4
        'TJ_shows',                 ##      222     NUMERIC         9999            4
        'TJ_roi',                   ##      223     NUMERIC         9999            4  $2ROI

        'days_since_last_race',     ##      224     NUMERIC         9999            4

        'race_conditions_1',        ##      225     CHARACTER                       254     Sometimes blank CONCATENATE THIS STRING?
        'race_conditions_2',        ##      226     CHARACTER                       254     because data is
        'race_conditions_3',        ##      227     CHARACTER                       254     not always available
        'race_conditions_4',        ##      228     CHARACTER                       254     Use field # 16 if necessary
        'race_conditions_5',        ##      229     CHARACTER                       254
        'race_conditions_6',        ##      230     CHARACTER                       254

        'life_starts_alw',          ##      231                     999             3
        'life_wins_alw',            ##      232                     999             3
        'life_places_alw',          ##      233                     999             3
        'life_shows_alw',           ##      234                     999             3
        'life_earnings_alw',        ##      235                     99999999        8
        'best_bris_speed_alw',      ##      236                     999             3

        'reserved237',              ##      237

        'low_claiming_price',       ##      238     NUMERIC         9999999         7       For today's race
        'statebread_flag',          ##      239     CHARACTER       X               1       For today's race

        'wager_type_1',             ##      240     CHARACTER       X(50)           50      For today's race if available
        'wager_type_2',             ##      241     CHARACTER       X(50)           50
        'wager_type_3',             ##      242     CHARACTER       X(50)           50
        'wager_type_4',             ##      243     CHARACTER       X(50)           50
        'wager_type_5',             ##      244     CHARACTER       X(50)           50
        'wager_type_6',             ##      245     CHARACTER       X(50)           50
        'wager_type_7',             ##      246     CHARACTER       X(50)           50
        'wager_type_8',             ##      247     CHARACTER       X(50)           50
        'wager_type_9',             ##      248     CHARACTER       X(50)           50

        'reserved249',              ##      249     CHARACTER       X(58)           58
        'reserved250',              ##      250     CHARACTER       X(12)           12

        'bris_prime_power',         ##      251     NUMERIC         999.99          6

        'reserved252',              ##      252
        'reserved253',              ##      253
        'reserved254',              ##      254
        'reserved255',              ##      255

        ##      *** Horse's Past Performace Data for last 10 races ***
        ##      For each of the last 10 races (most recent to furthest back):

        'past_race_date_1',         ##      256     CHARACTER       XXXXXXXX                8
        'past_race_date_2',         ##      257     CHARACTER       XXXXXXXX                8
        'past_race_date_3',         ##      258     CHARACTER       XXXXXXXX                8
        'past_race_date_4',         ##      259     CHARACTER       XXXXXXXX                8
        'past_race_date_5',         ##      260     CHARACTER       XXXXXXXX                8
        'past_race_date_6',         ##      261     CHARACTER       XXXXXXXX                8
        'past_race_date_7',         ##      262     CHARACTER       XXXXXXXX                8
        'past_race_date_8',         ##      263     CHARACTER       XXXXXXXX                8
        'past_race_date_9',         ##      264     CHARACTER       XXXXXXXX                8
        'past_race_date_10',        ##      265     CHARACTER       XXXXXXXX                8

        'past_days_since_last_1',   ##      266     NUMERIC         9999                    4       Blank-First timer
        'past_days_since_last_2',   ##      267     NUMERIC         9999                    4
        'past_days_since_last_3',   ##      268     NUMERIC         9999                    4
        'past_days_since_last_4',   ##      269     NUMERIC         9999                    4
        'past_days_since_last_5',   ##      270     NUMERIC         9999                    4
        'past_days_since_last_6',   ##      271     NUMERIC         9999                    4
        'past_days_since_last_7',   ##      272     NUMERIC         9999                    4
        'past_days_since_last_8',   ##      273     NUMERIC         9999                    4
        'past_days_since_last_9',   ##      274     NUMERIC         9999                    4
        'past_days_since_last_10',              ##      275                                             (# days since prev. race
                                    ##                                                      for 10th race back might
                                    ##                                                      not be available)
        'past_track_code_1',        ##      276     CHARACTER                       30
        'past_track_code_2',        ##      277     CHARACTER                       30
        'past_track_code_3',        ##      278     CHARACTER                       30
        'past_track_code_4',        ##      279     CHARACTER                       30
        'past_track_code_5',        ##      280     CHARACTER                       30
        'past_track_code_6',        ##      281     CHARACTER                       30
        'past_track_code_7',        ##      282     CHARACTER                       30
        'past_track_code_8',        ##      283     CHARACTER                       30
        'past_track_code_9',        ##      284     CHARACTER                       30
        'past_track_code_10',       ##      285     CHARACTER                       30

        'past_BRIS_track_code_1',   ##      286     CHARACTER                       30
        'past_BRIS_track_code_2',   ##      287     CHARACTER                       30
        'past_BRIS_track_code_3',   ##      288     CHARACTER                       30
        'past_BRIS_track_code_4',   ##      289     CHARACTER                       30
        'past_BRIS_track_code_5',   ##      290     CHARACTER                       30
        'past_BRIS_track_code_6',   ##      291     CHARACTER                       30
        'past_BRIS_track_code_7',   ##      292     CHARACTER                       30
        'past_BRIS_track_code_8',   ##      293     CHARACTER                       30
        'past_BRIS_track_code_9',   ##      294     CHARACTER                       30
        'past_BRIS_track_code_10',  ##      295     CHARACTER                       30

        'past_race_number_1',       ##      296     NUMERIC         99              2
        'past_race_number_2',       ##      297     NUMERIC         99              2
        'past_race_number_3',       ##      298     NUMERIC         99              2
        'past_race_number_4',       ##      299     NUMERIC         99              2
        'past_race_number_5',       ##      300     NUMERIC         99              2
        'past_race_number_6',       ##      301     NUMERIC         99              2
        'past_race_number_7',       ##      302     NUMERIC         99              2
        'past_race_number_8',       ##      303     NUMERIC         99              2
        'past_race_number_9',       ##      304     NUMERIC         99              2
        'past_race_number_10',      ##      305     NUMERIC         99              2

        'past_track_cond_1',        ##      306     CHARACTER       XX              2
        'past_track_cond_2',        ##      307     CHARACTER       XX              2
        'past_track_cond_3',        ##      308     CHARACTER       XX              2
        'past_track_cond_4',        ##      309     CHARACTER       XX              2
        'past_track_cond_5',        ##      310     CHARACTER       XX              2
        'past_track_cond_6',        ##      311     CHARACTER       XX              2
        'past_track_cond_7',        ##      312     CHARACTER       XX              2
        'past_track_cond_8',        ##      313     CHARACTER       XX              2
        'past_track_cond_9',        ##      314     CHARACTER       XX              2
        'past_track_cond_10',       ##      315     CHARACTER       XX              2

        'past_distance_1',          ##      316     NUMERIC         XX              5       In yards. Negative value
        'past_distance_2',          ##      317     NUMERIC         XX              5       for about distances
        'past_distance_3',          ##      318     NUMERIC         XX              5
        'past_distance_4',          ##      319     NUMERIC         XX              5
        'past_distance_5',          ##      320     NUMERIC         XX              5
        'past_distance_6',          ##      321     NUMERIC         XX              5
        'past_distance_7',          ##      322     NUMERIC         XX              5
        'past_distance_8',          ##      323     NUMERIC         XX              5
        'past_distance_9',          ##      324     NUMERIC         XX              5
        'past_distance_10',         ##      325     NUMERIC         XX              5

        'past_surface_1',           ##      326     CHARACTER       X               1       See field 7
        'past_surface_2',           ##      327     CHARACTER       X               1
        'past_surface_3',           ##      328     CHARACTER       X               1
        'past_surface_4',           ##      329     CHARACTER       X               1
        'past_surface_5',           ##      330     CHARACTER       X               1
        'past_surface_6',           ##      331     CHARACTER       X               1
        'past_surface_7',           ##      332     CHARACTER       X               1
        'past_surface_8',           ##      333     CHARACTER       X               1
        'past_surface_9',           ##      334     CHARACTER       X               1
        'past_surface_10',          ##      335     CHARACTER       X               1

        ##      Special Chute Indicator
        'past_special_chute_1',     ##      336     CHARACTER       X               1       c - chute
        'past_special_chute_2',     ##      337     CHARACTER       X               1
        'past_special_chute_3',     ##      338     CHARACTER       X               1
        'past_special_chute_4',     ##      339     CHARACTER       X               1
        'past_special_chute_5',     ##      340     CHARACTER       X               1
        'past_special_chute_6',     ##      341     CHARACTER       X               1
        'past_special_chute_7',     ##      342     CHARACTER       X               1
        'past_special_chute_8',     ##      343     CHARACTER       X               1
        'past_special_chute_9',     ##      344     CHARACTER       X               1
        'past_special_chute_10',    ##      345     CHARACTER       X               1

        ## Number of entrants
        'past_entrants_1',          ##      346     NUMERIC         99              2
        'past_entrants_2',          ##      347     NUMERIC         99              2
        'past_entrants_3',          ##      348     NUMERIC         99              2
        'past_entrants_4',          ##      349     NUMERIC         99              2
        'past_entrants_5',          ##      350     NUMERIC         99              2
        'past_entrants_6',          ##      351     NUMERIC         99              2
        'past_entrants_7',          ##      352     NUMERIC         99              2
        'past_entrants_8',          ##      353     NUMERIC         99              2
        'past_entrants_9',          ##      354     NUMERIC         99              2
        'past_entrants_10',         ##      355     NUMERIC         99              2

        ##      Past post position

        'past_post_1',              ##      356     NUMERIC         99              2
        'past_post_2',              ##      357     NUMERIC         99              2
        'past_post_3',              ##      358     NUMERIC         99              2
        'past_post_4',              ##      359     NUMERIC         99              2
        'past_post_5',              ##      360     NUMERIC         99              2
        'past_post_6',              ##      361     NUMERIC         99              2
        'past_post_7',              ##      362     NUMERIC         99              2
        'past_post_8',              ##      363     NUMERIC         99              2
        'past_post_9',              ##      364     NUMERIC         99              2
        'past_post_10',             ##      365     NUMERIC         99              2

        ## Equipment                                                                    b - blinkers
        'past_equipment_1',         ##      366     CHARACTER       X               1
        'past_equipment_2',         ##      367     CHARACTER       X               1
        'past_equipment_3',         ##      368     CHARACTER       X               1
        'past_equipment_4',         ##      369     CHARACTER       X               1
        'past_equipment_5',         ##      370     CHARACTER       X               1
        'past_equipment_6',         ##      371     CHARACTER       X               1
        'past_equipment_7',         ##      372     CHARACTER       X               1
        'past_equipment_8',         ##      373     CHARACTER       X               1
        'past_equipment_9',         ##      374     CHARACTER       X               1
        'past_equipment_10',        ##      375     CHARACTER       X               1

        ##      Race name of previous races
        'past_race_name_1',         ##      376
        'past_race_name_2',         ##      377
        'past_race_name_3',         ##      378
        'past_race_name_4',         ##      379
        'past_race_name_5',         ##      380
        'past_race_name_6',         ##      381
        'past_race_name_7',         ##      382
        'past_race_name_8',         ##      383
        'past_race_name_9',         ##      384
        'past_race_name_10',        ##      385

        ##      Medication
        'past_medication_1',        ##      386     NUMERIC        9       1       See also field #62
        'past_medication_2',        ##      387     NUMERIC        9       1       0=None
        'past_medication_3',        ##      388     NUMERIC        9       1       1=Lasix
        'past_medication_4',        ##      389     NUMERIC        9       1       2=Bute
        'past_medication_5',        ##      390     NUMERIC        9       1       3=Bute & Lasix
        'past_medication_6',        ##      391     NUMERIC        9       1
        'past_medication_7',        ##      392     NUMERIC        9       1
        'past_medication_8',        ##      393     NUMERIC        9       1
        'past_medication_9',        ##      394     NUMERIC        9       1
        'past_medication_10',       ##      395     NUMERIC        9       1

        ##      Trip Comment
        'past_trip_comment_1',      ##      396     CHARACTER               100
        'past_trip_comment_2',      ##      397     CHARACTER               100
        'past_trip_comment_3',      ##      398     CHARACTER               100
        'past_trip_comment_4',      ##      399     CHARACTER               100
        'past_trip_comment_5',      ##      400     CHARACTER               100
        'past_trip_comment_6',      ##      401     CHARACTER               100
        'past_trip_comment_7',      ##      402     CHARACTER               100
        'past_trip_comment_8',      ##      403     CHARACTER               100
        'past_trip_comment_9',      ##      404     CHARACTER               100
        'past_trip_comment_10',     ##      405     CHARACTER               100

        ##      Winner, Place, and Show horse names
        'past_win_1',               ##      406     CHARACTER
        'past_win_2',               ##      407     CHARACTER
        'past_win_3',               ##      408     CHARACTER
        'past_win_4',               ##      409     CHARACTER
        'past_win_5',               ##      410     CHARACTER
        'past_win_6',               ##      411     CHARACTER
        'past_win_7',               ##      412     CHARACTER
        'past_win_8',               ##      413     CHARACTER
        'past_win_9',               ##      414     CHARACTER
        'past_win_10',              ##      415     CHARACTER

        'past_place_1',             ##      416     Character
        'past_place_2',             ##      417     Character
        'past_place_3',             ##      418     Character
        'past_place_4',             ##      419     Character
        'past_place_5',             ##      420     Character
        'past_place_6',             ##      421     Character
        'past_place_7',             ##      422     Character
        'past_place_8',             ##      423     Character
        'past_place_9',             ##      424     Character
        'past_place_10',            ##      425     Character

        'past_show_1',              ##      426     Character
        'past_show_2',              ##      427     Character
        'past_show_3',              ##      428     Character
        'past_show_4',              ##      429     Character
        'past_show_5',              ##      430     Character
        'past_show_6',              ##      431     Character
        'past_show_7',              ##      432     Character
        'past_show_8',              ##      433     Character
        'past_show_9',              ##      434     Character
        'past_show_10',             ##      435     Character

        ##      Winner, PLcae, and Show Weight Carried

        'past_win_weight_1',        ##      436     NUMERIC         999     3
        'past_win_weight_2',        ##      437     NUMERIC         999     3
        'past_win_weight_3',        ##      438     NUMERIC         999     3
        'past_win_weight_4',        ##      439     NUMERIC         999     3
        'past_win_weight_5',        ##      440     NUMERIC         999     3
        'past_win_weight_6',        ##      441     NUMERIC         999     3
        'past_win_weight_7',        ##      442     NUMERIC         999     3
        'past_win_weight_8',        ##      443     NUMERIC         999     3
        'past_win_weight_9',        ##      444     NUMERIC         999     3
        'past_win_weight_10',       ##      445     NUMERIC         999     3

        'past_place_weight_1',      ##      446     NUMERIC         999     3
        'past_place_weight_2',      ##      447     NUMERIC         999     3
        'past_place_weight_3',      ##      448     NUMERIC         999     3
        'past_place_weight_4',      ##      449     NUMERIC         999     3
        'past_place_weight_5',      ##      450     NUMERIC         999     3
        'past_place_weight_6',      ##      451     NUMERIC         999     3
        'past_place_weight_7',      ##      452     NUMERIC         999     3
        'past_place_weight_8',      ##      453     NUMERIC         999     3
        'past_place_weight_9',      ##      454     NUMERIC         999     3
        'past_place_weight_10',     ##      455     NUMERIC         999     3

        'past_show_weight_1',       ##      456     NUMERIC         999     3
        'past_show_weight_2',       ##      457     NUMERIC         999     3
        'past_show_weight_3',       ##      458     NUMERIC         999     3
        'past_show_weight_4',       ##      459     NUMERIC         999     3
        'past_show_weight_5',       ##      460     NUMERIC         999     3
        'past_show_weight_6',       ##      461     NUMERIC         999     3
        'past_show_weight_7',       ##      462     NUMERIC         999     3
        'past_show_weight_8',       ##      463     NUMERIC         999     3
        'past_show_weight_9',       ##      464     NUMERIC         999     3
        'past_show_weight_10',      ##      465     NUMERIC         999     3

        ##      Past Winner, Place, and Show Margins

        'past_win_margin_1',        ##      466     NUMERIC         99.99   5       (0 if Dead Heat)
        'past_win_margin_2',        ##      467     NUMERIC         99.99   5
        'past_win_margin_3',        ##      468     NUMERIC         99.99   5
        'past_win_margin_4',        ##      469     NUMERIC         99.99   5
        'past_win_margin_5',        ##      470     NUMERIC         99.99   5
        'past_win_margin_6',        ##      471     NUMERIC         99.99   5
        'past_win_margin_7',        ##      472     NUMERIC         99.99   5
        'past_win_margin_8',        ##      473     NUMERIC         99.99   5
        'past_win_margin_9',        ##      474     NUMERIC         99.99   5
        'past_win_margin_10',       ##      475     NUMERIC         99.99   5

        'past_place_margin_1',      ##      476     NUMERIC         99.99   5
        'past_place_margin_2',      ##      477     NUMERIC         99.99   5
        'past_place_margin_3',      ##      478     NUMERIC         99.99   5
        'past_place_margin_4',      ##      479     NUMERIC         99.99   5
        'past_place_margin_5',      ##      480     NUMERIC         99.99   5
        'past_place_margin_6',      ##      481     NUMERIC         99.99   5
        'past_place_margin_7',      ##      482     NUMERIC         99.99   5
        'past_place_margin_8',      ##      483     NUMERIC         99.99   5
        'past_place_margin_9',      ##      484     NUMERIC         99.99   5
        'past_place_margin_10',     ##      485     NUMERIC         99.99   5

        'past_show_margin_1',       ##      486     NUMERIC         99.99   5
        'past_show_margin_2',       ##      487     NUMERIC         99.99   5
        'past_show_margin_3',       ##      488     NUMERIC         99.99   5
        'past_show_margin_4',       ##      489     NUMERIC         99.99   5
        'past_show_margin_5',       ##      490     NUMERIC         99.99   5
        'past_show_margin_6',       ##      491     NUMERIC         99.99   5
        'past_show_margin_7',       ##      492     NUMERIC         99.99   5
        'past_show_margin_8',       ##      493     NUMERIC         99.99   5
        'past_show_margin_9',       ##      494     NUMERIC         99.99   5
        'past_show_margin_10',      ##      495     NUMERIC         99.99   5

        ##      Alternate/Extra Comment Line

        'past_extra_comment_1',     ##      496     CHARACTER               200     Includes 'claimed from' text &
        'past_extra_comment_2',     ##      497     CHARACTER               200     Misc. other comments
        'past_extra_comment_3',     ##      498     CHARACTER               200
        'past_extra_comment_4',     ##      499     CHARACTER               200
        'past_extra_comment_5',     ##      500     CHARACTER               200
        'past_extra_comment_6',     ##      501     CHARACTER               200
        'past_extra_comment_7',     ##      502     CHARACTER               200
        'past_extra_comment_8',     ##      503     CHARACTER               200
        'past_extra_comment_9',     ##      504     CHARACTER               200
        'past_extra_comment_10',    ##      505     CHARACTER               200

        'past_weight_1',            ##      506     NUMERIC         999     3
        'past_weight_2',            ##      507     NUMERIC         999     3
        'past_weight_3',            ##      508     NUMERIC         999     3
        'past_weight_4',            ##      509     NUMERIC         999     3
        'past_weight_5',            ##      510     NUMERIC         999     3
        'past_weight_6',            ##      511     NUMERIC         999     3
        'past_weight_7',            ##      512     NUMERIC         999     3
        'past_weight_8',            ##      513     NUMERIC         999     3
        'past_weight_9',            ##      514     NUMERIC         999     3
        'past_weight_10',           ##      515     NUMERIC         999     3

        'past_odds_1',              ##      516     NUMERIC         9999.99 7
        'past_odds_2',              ##      517     NUMERIC         9999.99 7
        'past_odds_3',              ##      518     NUMERIC         9999.99 7
        'past_odds_4',              ##      519     NUMERIC         9999.99 7
        'past_odds_5',              ##      520     NUMERIC         9999.99 7
        'past_odds_6',              ##      521     NUMERIC         9999.99 7
        'past_odds_7',              ##      522     NUMERIC         9999.99 7
        'past_odds_8',              ##      523     NUMERIC         9999.99 7
        'past_odds_9',              ##      524     NUMERIC         9999.99 7
        'past_odds_10',             ##      525     NUMERIC         9999.99 7

        'past_entry_1',             ##      526     CHARACTER      X       1       e- entry
        'past_entry_2',             ##      527     CHARACTER      X       1
        'past_entry_3',             ##      528     CHARACTER      X       1
        'past_entry_4',             ##      529     CHARACTER      X       1
        'past_entry_5',             ##      530     CHARACTER      X       1
        'past_entry_6',             ##      531     CHARACTER      X       1
        'past_entry_7',             ##      532     CHARACTER      X       1
        'past_entry_8',             ##      533     CHARACTER      X       1
        'past_entry_9',             ##      534     CHARACTER      X       1
        'past_entry_10',            ##      535     CHARACTER      X       1

        'past_race_class_1',        ##      536     CHARACTER               25
        'past_race_class_2',        ##      537     CHARACTER               25
        'past_race_class_3',        ##      538     CHARACTER               25
        'past_race_class_4',        ##      539     CHARACTER               25
        'past_race_class_5',        ##      540     CHARACTER               25
        'past_race_class_6',        ##      541     CHARACTER               25
        'past_race_class_7',        ##      542     CHARACTER               25
        'past_race_class_8',        ##      543     CHARACTER               25
        'past_race_class_9',        ##      544     CHARACTER               25
        'past_race_class_10',       ##      545     CHARACTER               25

        ##      Claiming Price (of horse)
        'past_claim_price_1',       ##      546     NUMERIC         9999999         7
        'past_claim_price_2',       ##      547     NUMERIC         9999999         7
        'past_claim_price_3',       ##      548     NUMERIC         9999999         7
        'past_claim_price_4',       ##      549     NUMERIC         9999999         7
        'past_claim_price_5',       ##      550     NUMERIC         9999999         7
        'past_claim_price_6',       ##      551     NUMERIC         9999999         7
        'past_claim_price_7',       ##      552     NUMERIC         9999999         7
        'past_claim_price_8',       ##      553     NUMERIC         9999999         7
        'past_claim_price_9',       ##      554     NUMERIC         9999999         7
        'past_claim_price_10',      ##      555     NUMERIC         9999999         7

        'past_purse_1',             ##      556     NUMERIC         99999999        8
        'past_purse_2',             ##      557     NUMERIC         99999999        8
        'past_purse_3',             ##      558     NUMERIC         99999999        8
        'past_purse_4',             ##      559     NUMERIC         99999999        8
        'past_purse_5',             ##      560     NUMERIC         99999999        8
        'past_purse_6',             ##      561     NUMERIC         99999999        8
        'past_purse_7',             ##      562     NUMERIC         99999999        8
        'past_purse_8',             ##      563     NUMERIC         99999999        8
        'past_purse_9',             ##      564     NUMERIC         99999999        8
        'past_purse_10',            ##      565     NUMERIC         99999999        8

        ##      Start call position
        'past_call_pos_start_1',    ##      566     CHARACTER                       2       A- Bled
        'past_call_pos_start_2',    ##      567     CHARACTER                       2       B- Bolted
        'past_call_pos_start_3',    ##      568     CHARACTER                       2       C- Broke down
        'past_call_pos_start_4',    ##      569     CHARACTER                       2       D- Distanced
        'past_call_pos_start_5',    ##      570     CHARACTER                       2       E- Dwelt
        'past_call_pos_start_6',    ##      571     CHARACTER                       2       F- Eased
        'past_call_pos_start_7',    ##      572     CHARACTER                       2       G- Fell
        'past_call_pos_start_8',    ##      573     CHARACTER                       2       H- Lame
        'past_call_pos_start_9',    ##      574     CHARACTER                       2       I- Left at post
        'past_call_pos_start_10',   ##      575     CHARACTER                       2       J- Left course

        'past_call_pos_first_1',    ##      576     CHARACTER                       2       K- Lost rider
        'past_call_pos_first_2',    ##      577     CHARACTER                       2       L- Running positions ommitted
        'past_call_pos_first_3',    ##      578     CHARACTER                       2          b/c of weather
        'past_call_pos_first_4',    ##      579     CHARACTER                       2       M- Propped
        'past_call_pos_first_5',    ##      580     CHARACTER                       2       N- Sulked
        'past_call_pos_first_6',    ##      581     CHARACTER                       2       O- Sore
        'past_call_pos_first_7',    ##      582     CHARACTER                       2       P- Refused to break
        'past_call_pos_first_8',    ##      583     CHARACTER                       2       Q- Pulled up
        'past_call_pos_first_9',    ##      584     CHARACTER                       2       R- Wheeled
        'past_call_pos_first_10',   ##      585     CHARACTER                       2       S- Saddle slopped

        'past_call_pos_second_1',   ##      586     CHARACTER                       2       T- Lost irons
        'past_call_pos_second_2',   ##      587     CHARACTER                       2       U- Beaten off
        'past_call_pos_second_3',   ##      588     CHARACTER                       2       V- Reared
        'past_call_pos_second_4',   ##      589     CHARACTER                       2       W- Bucked
        'past_call_pos_second_5',   ##      590     CHARACTER                       2       X- Did not finish
        'past_call_pos_second_6',   ##      591     CHARACTER                       2       Y- Unplaced
        'past_call_pos_second_7',   ##      592     CHARACTER                       2       ? or *- Unspecified reason
        'past_call_pos_second_8',   ##      593     CHARACTER                       2               for missed call
        'past_call_pos_second_9',   ##      574     CHARACTER                       2
        'past_call_pos_second_10',  ##      595     CHARACTER                       2

        'past_call_pos_gate_1',     ##      596     CHARACTER                       2
        'past_call_pos_gate_2',     ##      597     CHARACTER                       2
        'past_call_pos_gate_3',     ##      598     CHARACTER                       2
        'past_call_pos_gate_4',     ##      599     CHARACTER                       2
        'past_call_pos_gate_5',     ##      600     CHARACTER                       2
        'past_call_pos_gate_6',     ##      601     CHARACTER                       2
        'past_call_pos_gate_7',     ##      602     CHARACTER                       2
        'past_call_pos_gate_8',     ##      603     CHARACTER                       2
        'past_call_pos_gate_9',     ##      604     CHARACTER                       2
        'past_call_pos_gate_10',    ##      605     CHARACTER                       2

        'past_call_pos_stretch_1',  ##      606     CHARACTER                       2
        'past_call_pos_stretch_2',  ##      607     CHARACTER                       2
        'past_call_pos_stretch_3',  ##      608     CHARACTER                       2
        'past_call_pos_stretch_4',  ##      609     CHARACTER                       2
        'past_call_pos_stretch_5',  ##      610     CHARACTER                       2
        'past_call_pos_stretch_6',  ##      611     CHARACTER                       2
        'past_call_pos_stretch_7',  ##      612     CHARACTER                       2
        'past_call_pos_stretch_8',  ##      613     CHARACTER                       2
        'past_call_pos_stretch_9',  ##      614     CHARACTER                       2
        'past_call_pos_stretch_10',  ##      615     CHARACTER                       2

        'past_call_pos_finish_1',   ##      616     CHARACTER                       2
        'past_call_pos_finish_2',   ##      617     CHARACTER                       2
        'past_call_pos_finish_3',   ##      618     CHARACTER                       2
        'past_call_pos_finish_4',   ##      619     CHARACTER                       2
        'past_call_pos_finish_5',   ##      620     CHARACTER                       2
        'past_call_pos_finish_6',   ##      621     CHARACTER                       2
        'past_call_pos_finish_7',   ##      622     CHARACTER                       2
        'past_call_pos_finish_8',   ##      623     CHARACTER                       2
        'past_call_pos_finish_9',   ##      624     CHARACTER                       2
        'past_call_pos_finish_10',  ##      625     CHARACTER                       2

        'past_money_pos_1',         ##      626     CHARACTER                       2
        'past_money_pos_2',         ##      627     CHARACTER                       2
        'past_money_pos_3',         ##      628     CHARACTER                       2
        'past_money_pos_4',         ##      629     CHARACTER                       2
        'past_money_pos_5',         ##      630     CHARACTER                       2
        'past_money_pos_6',         ##      631     CHARACTER                       2
        'past_money_pos_7',         ##      632     CHARACTER                       2
        'past_money_pos_8',         ##      633     CHARACTER                       2
        'past_money_pos_9',         ##      634     CHARACTER                       2
        'past_money_pos_10',        ##      635     CHARACTER                       2

        ##      Start Call - Beaten lengths/Leader margin
        'past_lead_margin_start_1', ##      636                     99.99           5
        'past_lead_margin_start_2', ##      637                     99.99           5
        'past_lead_margin_start_3', ##      638                     99.99           5
        'past_lead_margin_start_4', ##      639                     99.99           5
        'past_lead_margin_start_5', ##      640                     99.99           5
        'past_lead_margin_start_6', ##      641                     99.99           5
        'past_lead_margin_start_7', ##      642                     99.99           5
        'past_lead_margin_start_8', ##      643                     99.99           5
        'past_lead_margin_start_9', ##      644                     99.99           5
        'past_lead_margin_start_10',##      645                     99.99           5

        ##      Start Call - Beaten lengths only
        'past_beaten_lengths_start_1',      ##      646                     99.99           5
        'past_beaten_lengths_start_2',      ##      647                     99.99           5
        'past_beaten_lengths_start_3',      ##      648                     99.99           5
        'past_beaten_lengths_start_4',      ##      649                     99.99           5
        'past_beaten_lengths_start_5',      ##      650                     99.99           5
        'past_beaten_lengths_start_6',      ##      651                     99.99           5
        'past_beaten_lengths_start_7',      ##      652                     99.99           5
        'past_beaten_lengths_start_8',      ##      653                     99.99           5
        'past_beaten_lengths_start_9',      ##      654                     99.99           5
        'past_beaten_lengths_start_10',     ##      655                     99.99           5

        ##      1st Call Beaten lengths/Leader margin
        'past_lead_margin_first_call_1',    ##      656                     99.99           5
        'past_lead_margin_first_call_2',    ##      657                     99.99           5
        'past_lead_margin_first_call_3',    ##      658                     99.99           5
        'past_lead_margin_first_call_4',    ##      659                     99.99           5
        'past_lead_margin_first_call_5',    ##      660                     99.99           5
        'past_lead_margin_first_call_6',    ##      661                     99.99           5
        'past_lead_margin_first_call_7',    ##      662                     99.99           5
        'past_lead_margin_first_call_8',    ##      663                     99.99           5
        'past_lead_margin_first_call_9',    ##      664                     99.99           5
        'past_lead_margin_first_call_10',   ##      665                     99.99           5

        ##      1st Call Beathen lengths only
        'past_beaten_lengths_first_call_1', ##      666                     99.99           5
        'past_beaten_lengths_first_call_2', ##      667                     99.99           5
        'past_beaten_lengths_first_call_3', ##      668                     99.99           5
        'past_beaten_lengths_first_call_4', ##      669                     99.99           5
        'past_beaten_lengths_first_call_5', ##      670                     99.99           5
        'past_beaten_lengths_first_call_6', ##      671                     99.99           5
        'past_beaten_lengths_first_call_7', ##      672                     99.99           5
        'past_beaten_lengths_first_call_8', ##      673                     99.99           5
        'past_beaten_lengths_first_call_9', ##      674                     99.99           5
        'past_beaten_lengths_first_call_10',##      675                     99.99           5

        ##      2d Call Beaten Lengths/Leader marbin
        'past_lead_margin_second_call_1',   ##      676                     99.99           5
        'past_lead_margin_second_call_2',   ##      677                     99.99           5
        'past_lead_margin_second_call_3',   ##      678                     99.99           5
        'past_lead_margin_second_call_4',   ##      679                     99.99           5
        'past_lead_margin_second_call_5',   ##      680                     99.99           5
        'past_lead_margin_second_call_6',   ##      681                     99.99           5
        'past_lead_margin_second_call_7',   ##      682                     99.99           5
        'past_lead_margin_second_call_8',   ##      683                     99.99           5
        'past_lead_margin_second_call_9',   ##      684                     99.99           5
        'past_lead_margin_second_call_10',  ##      685                     99.99           5

        ##      2d Call Beath lengths only
        'past_beaten_lengths_second_call_1',    ##      686                     99.99           5
        'past_beaten_lengths_second_call_2',    ##      687                     99.99           5
        'past_beaten_lengths_second_call_3',    ##      688                     99.99           5
        'past_beaten_lengths_second_call_4',    ##      689                     99.99           5
        'past_beaten_lengths_second_call_5',    ##      690                     99.99           5
        'past_beaten_lengths_second_call_6',    ##      691                     99.99           5
        'past_beaten_lengths_second_call_7',    ##      692                     99.99           5
        'past_beaten_lengths_second_call_8',    ##      693                     99.99           5
        'past_beaten_lengths_second_call_9',    ##      694                     99.99           5
        'past_beaten_lengths_second_call_10',   ##      695                     99.99           5

        ##      BRIS Race Shape- 1st Call
        'past_bris_shape_first_call_1',         ##      696                     999             3
        'past_bris_shape_first_call_2',         ##      697                     999             3
        'past_bris_shape_first_call_3',         ##      698                     999             3
        'past_bris_shape_first_call_4',         ##      699                     999             3
        'past_bris_shape_first_call_5',         ##      700                     999             3
        'past_bris_shape_first_call_6',         ##      701                     999             3
        'past_bris_shape_first_call_7',         ##      702                     999             3
        'past_bris_shape_first_call_8',         ##      703                     999             3
        'past_bris_shape_first_call_9',         ##      704                     999             3
        'past_bris_shape_first_call_10',        ##      705                     999             3

        'reserved706',                          ##      706
        'reserved707',                          ##      707
        'reserved708',                          ##      708
        'reserved709',                          ##      709
        'reserved710',                          ##      710
        'reserved711',                          ##      711
        'reserved712',                          ##      712
        'reserved713',                          ##      713
        'reserved714',                          ##      714
        'reserved715',                          ##      715

        ##      Stretch beaten lengths/leader margin
        'past_lead_margin_stretch_call_1',      ##      716                     99.99           5
        'past_lead_margin_stretch_call_2',      ##      717                     99.99           5
        'past_lead_margin_stretch_call_3',      ##      718                     99.99           5
        'past_lead_margin_stretch_call_4',      ##      719                     99.99           5
        'past_lead_margin_stretch_call_5',      ##      720                     99.99           5
        'past_lead_margin_stretch_call_6',      ##      721                     99.99           5
        'past_lead_margin_stretch_call_7',      ##      722                     99.99           5
        'past_lead_margin_stretch_call_8',      ##      723                     99.99           5
        'past_lead_margin_stretch_call_9',      ##      724                     99.99           5
        'past_lead_margin_stretch_call_10',     ##      725                     99.99           5

        ##      Stretch beaten lengths only
        'past_beaten_lengths_stretch_call_1',   ##      726
        'past_beaten_lengths_stretch_call_2',   ##      727
        'past_beaten_lengths_stretch_call_3',   ##      728
        'past_beaten_lengths_stretch_call_4',   ##      729
        'past_beaten_lengths_stretch_call_5',   ##      730
        'past_beaten_lengths_stretch_call_6',   ##      731
        'past_beaten_lengths_stretch_call_7',   ##      732
        'past_beaten_lengths_stretch_call_8',   ##      733
        'past_beaten_lengths_stretch_call_9',   ##      734
        'past_beaten_lengths_stretch_call_10',  ##      735

        ## Finish Beaten lengths/leader margin
        'past_lead_margin_finish_1',            ##      736     NUMERIC         99.99           5
        'past_lead_margin_finish_2',            ##      737     NUMERIC         99.99           5
        'past_lead_margin_finish_3',            ##      738     NUMERIC         99.99           5
        'past_lead_margin_finish_4',            ##      739     NUMERIC         99.99           5
        'past_lead_margin_finish_5',            ##      740     NUMERIC         99.99           5
        'past_lead_margin_finish_6',            ##      741     NUMERIC         99.99           5
        'past_lead_margin_finish_7',            ##      742     NUMERIC         99.99           5
        'past_lead_margin_finish_8',            ##      743     NUMERIC         99.99           5
        'past_lead_margin_finish_9',            ##      744     NUMERIC         99.99           5
        'past_lead_margin_finish_10',           ##      745     NUMERIC         99.99           5

        ##      Finish beaten lengths only
        'past_beaten_lengths_finish_1',         ##      746
        'past_beaten_lengths_finish_2',         ##      747
        'past_beaten_lengths_finish_3',         ##      748
        'past_beaten_lengths_finish_4',         ##      749
        'past_beaten_lengths_finish_5',         ##      750
        'past_beaten_lengths_finish_6',         ##      751
        'past_beaten_lengths_finish_7',         ##      752
        'past_beaten_lengths_finish_8',         ##      753
        'past_beaten_lengths_finish_9',         ##      754
        'past_beaten_lengths_finish_10',        ##      755

        ##      BRIS Race Shape 2d Call
        'past_bris_shape_second_call_1',        ##      756     NUMERIC         999             3
        'past_bris_shape_second_call_2',        ##      757     NUMERIC         999             3
        'past_bris_shape_second_call_3',        ##      758     NUMERIC         999             3
        'past_bris_shape_second_call_4',        ##      759     NUMERIC         999             3
        'past_bris_shape_second_call_5',        ##      760     NUMERIC         999             3
        'past_bris_shape_second_call_6',        ##      761     NUMERIC         999             3
        'past_bris_shape_second_call_7',        ##      762     NUMERIC         999             3
        'past_bris_shape_second_call_8',        ##      763     NUMERIC         999             3
        'past_bris_shape_second_call_9',        ##      764     NUMERIC         999             3
        'past_bris_shape_second_call_10',       ##      765     NUMERIC         999             3

        ##      BRIS Pace Figures
        'past_bris_pace_2f_1',                  ##      766     NUMERIC         999             3
        'past_bris_pace_2f_2',                  ##      767     NUMERIC         999             3
        'past_bris_pace_2f_3',                  ##      768     NUMERIC         999             3
        'past_bris_pace_2f_4',                  ##      769     NUMERIC         999             3
        'past_bris_pace_2f_5',                  ##      770     NUMERIC         999             3
        'past_bris_pace_2f_6',                  ##      771     NUMERIC         999             3
        'past_bris_pace_2f_7',                  ##      772     NUMERIC         999             3
        'past_bris_pace_2f_8',                  ##      773     NUMERIC         999             3
        'past_bris_pace_2f_9',                  ##      774     NUMERIC         999             3
        'past_bris_pace_2f_10',                 ##      775     NUMERIC         999             3

        'past_bris_pace_4f_1',                  ##      776     NUMERIC         999             3
        'past_bris_pace_4f_2',                  ##      777     NUMERIC         999             3
        'past_bris_pace_4f_3',                  ##      778     NUMERIC         999             3
        'past_bris_pace_4f_4',                  ##      779     NUMERIC         999             3
        'past_bris_pace_4f_5',                  ##      780     NUMERIC         999             3
        'past_bris_pace_4f_6',                  ##      781     NUMERIC         999             3
        'past_bris_pace_4f_7',                  ##      782     NUMERIC         999             3
        'past_bris_pace_4f_8',                  ##      783     NUMERIC         999             3
        'past_bris_pace_4f_9',                  ##      784     NUMERIC         999             3
        'past_bris_pace_4f_10',                 ##      785     NUMERIC         999             3

        'past_bris_pace_6f_1',                  ##      786     NUMERIC         999             3
        'past_bris_pace_6f_2',                  ##      787     NUMERIC         999             3
        'past_bris_pace_6f_3',                  ##      788     NUMERIC         999             3
        'past_bris_pace_6f_4',                  ##      789     NUMERIC         999             3
        'past_bris_pace_6f_5',                  ##      790     NUMERIC         999             3
        'past_bris_pace_6f_6',                  ##      791     NUMERIC         999             3
        'past_bris_pace_6f_7',                  ##      792     NUMERIC         999             3
        'past_bris_pace_6f_8',                  ##      793     NUMERIC         999             3
        'past_bris_pace_6f_9',                  ##      794     NUMERIC         999             3
        'past_bris_pace_6f_10',                 ##      795     NUMERIC         999             3

        'past_bris_pace_8f_1',                  ##      796     NUMERIC         999             3
        'past_bris_pace_8f_2',                  ##      797     NUMERIC         999             3
        'past_bris_pace_8f_3',                  ##      798     NUMERIC         999             3
        'past_bris_pace_8f_4',                  ##      799     NUMERIC         999             3
        'past_bris_pace_8f_5',                  ##      800     NUMERIC         999             3
        'past_bris_pace_8f_6',                  ##      801     NUMERIC         999             3
        'past_bris_pace_8f_7',                  ##      802     NUMERIC         999             3
        'past_bris_pace_8f_8',                  ##      803     NUMERIC         999             3
        'past_bris_pace_8f_9',                  ##      804     NUMERIC         999             3
        'past_bris_pace_8f_10',                 ##      805     NUMERIC         999             3

        'past_bris_pace_10f_1',                 ##      806     NUMERIC         999             3
        'past_bris_pace_10f_2',                 ##      809     NUMERIC         999             3
        'past_bris_pace_10f_3',                 ##      808     NUMERIC         999             3
        'past_bris_pace_10f_4',                 ##      809     NUMERIC         999             3
        'past_bris_pace_10f_5',                 ##      810     NUMERIC         999             3
        'past_bris_pace_10f_6',                 ##      811     NUMERIC         999             3
        'past_bris_pace_10f_7',                 ##      812     NUMERIC         999             3
        'past_bris_pace_10f_8',                 ##      813     NUMERIC         999             3
        'past_bris_pace_10f_9',                 ##      814     NUMERIC         999             3
        'past_bris_pace_10f_10',                ##      815     NUMERIC         999             3

        'past_bris_pace_late_1',                ##      816     NUMERIC         999             3
        'past_bris_pace_late_2',                ##      817     NUMERIC         999             3
        'past_bris_pace_late_3',                ##      818     NUMERIC         999             3
        'past_bris_pace_late_4',                ##      819     NUMERIC         999             3
        'past_bris_pace_late_5',                ##      820     NUMERIC         999             3
        'past_bris_pace_late_6',                ##      821     NUMERIC         999             3
        'past_bris_pace_late_7',                ##      822     NUMERIC         999             3
        'past_bris_pace_late_8',                ##      823     NUMERIC         999             3
        'past_bris_pace_late_9',                ##      824     NUMERIC         999             3
        'past_bris_pace_late_10',               ##      825     NUMERIC         999             3

        'reserved826',                          ##      826
        'reserved827',                          ##      827
        'reserved828',                          ##      828
        'reserved829',                          ##      829
        'reserved830',                          ##      830
        'reserved831',                          ##      831
        'reserved832',                          ##      832
        'reserved833',                          ##      833
        'reserved834',                          ##      834
        'reserved835',                          ##      835
        'reserved836',                          ##      836
        'reserved837',                          ##      837
        'reserved838',                          ##      838
        'reserved839',                          ##      839
        'reserved840',                          ##      840
        'reserved841',                          ##      841
        'reserved842',                          ##      842
        'reserved843',                          ##      843
        'reserved844',                          ##      844
        'reserved845',                          ##      845

        ##      BRIS Speed Rating
        'past_bris_speed_rating_1',         ##      846     NUMERIC         999     3
        'past_bris_speed_rating_2',         ##      847     NUMERIC         999     3
        'past_bris_speed_rating_3',         ##      848     NUMERIC         999     3
        'past_bris_speed_rating_4',         ##      849     NUMERIC         999     3
        'past_bris_speed_rating_5',         ##      850     NUMERIC         999     3
        'past_bris_speed_rating_6',         ##      851     NUMERIC         999     3
        'past_bris_speed_rating_7',         ##      852     NUMERIC         999     3
        'past_bris_speed_rating_8',         ##      853     NUMERIC         999     3
        'past_bris_speed_rating_9',         ##      854     NUMERIC         999     3
        'past_bris_speed_rating_10',        ##      855     NUMERIC         999     3

        ##      Speed rating
        'past_speed_rating_1',              ##      856     NUMERIC         999     3
        'past_speed_rating_2',              ##      857     NUMERIC         999     3
        'past_speed_rating_3',              ##      858     NUMERIC         999     3
        'past_speed_rating_4',              ##      859     NUMERIC         999     3
        'past_speed_rating_5',              ##      860     NUMERIC         999     3
        'past_speed_rating_6',              ##      861     NUMERIC         999     3
        'past_speed_rating_7',              ##      862     NUMERIC         999     3
        'past_speed_rating_8',              ##      863     NUMERIC         999     3
        'past_speed_rating_9',              ##      864     NUMERIC         999     3
        'past_speed_rating_10',             ##      865     NUMERIC         999     3

        ##      Track Variant
        'past_track_variant_1',             ##      866     NUMERIC         99      2
        'past_track_variant_2',             ##      867     NUMERIC         99      2
        'past_track_variant_3',             ##      868     NUMERIC         99      2
        'past_track_variant_4',             ##      869     NUMERIC         99      2
        'past_track_variant_5',             ##      870     NUMERIC         99      2
        'past_track_variant_6',             ##      871     NUMERIC         99      2
        'past_track_variant_7',             ##      872     NUMERIC         99      2
        'past_track_variant_8',             ##      873     NUMERIC         99      2
        'past_track_variant_9',             ##      874     NUMERIC         99      2
        'past_track_variant_10',            ##      875     NUMERIC         99      2

        ## Past Fractions (seconds and hundreths)

        'past_fraction_2f_1',               ##      876     NUMERIC         999.99  6       Seconds & Hundreths
        'past_fraction_2f_2',               ##      877     NUMERIC         999.99  6
        'past_fraction_2f_3',               ##      878     NUMERIC         999.99  6
        'past_fraction_2f_4',               ##      879     NUMERIC         999.99  6
        'past_fraction_2f_5',               ##      880     NUMERIC         999.99  6
        'past_fraction_2f_6',               ##      881     NUMERIC         999.99  6
        'past_fraction_2f_7',               ##      882     NUMERIC         999.99  6
        'past_fraction_2f_8',               ##      883     NUMERIC         999.99  6
        'past_fraction_2f_9',               ##      884     NUMERIC         999.99  6
        'past_fraction_2f_10',              ##      885     NUMERIC         999.99  6

        'past_fraction_3f_1',               ##      886     NUMERIC         999.99  6
        'past_fraction_3f_2',               ##      887     NUMERIC         999.99  6
        'past_fraction_3f_3',               ##      888     NUMERIC         999.99  6
        'past_fraction_3f_4',               ##      889     NUMERIC         999.99  6
        'past_fraction_3f_5',               ##      890     NUMERIC         999.99  6
        'past_fraction_3f_6',               ##      891     NUMERIC         999.99  6
        'past_fraction_3f_7',               ##      892     NUMERIC         999.99  6
        'past_fraction_3f_8',               ##      893     NUMERIC         999.99  6
        'past_fraction_3f_9',               ##      894     NUMERIC         999.99  6
        'past_fraction_3f_10',              ##      895     NUMERIC         999.99  6

        'past_fraction_4f_1',               ##      896     NUMERIC         999.99  6
        'past_fraction_4f_2',               ##      897     NUMERIC         999.99  6
        'past_fraction_4f_3',               ##      898     NUMERIC         999.99  6
        'past_fraction_4f_4',               ##      899     NUMERIC         999.99  6
        'past_fraction_4f_5',               ##      900     NUMERIC         999.99  6
        'past_fraction_4f_6',               ##      901     NUMERIC         999.99  6
        'past_fraction_4f_7',               ##      902     NUMERIC         999.99  6
        'past_fraction_4f_8',               ##      903     NUMERIC         999.99  6
        'past_fraction_4f_9',               ##      904     NUMERIC         999.99  6
        'past_fraction_4f_10',              ##      905     NUMERIC         999.99  6

        'past_fraction_5f_1',               ##      906     NUMERIC         999.99  6
        'past_fraction_5f_2',               ##      907     NUMERIC         999.99  6
        'past_fraction_5f_3',               ##      908     NUMERIC         999.99  6
        'past_fraction_5f_4',               ##      909     NUMERIC         999.99  6
        'past_fraction_5f_5',               ##      910     NUMERIC         999.99  6
        'past_fraction_5f_6',               ##      911     NUMERIC         999.99  6
        'past_fraction_5f_7',               ##      912     NUMERIC         999.99  6
        'past_fraction_5f_8',               ##      913     NUMERIC         999.99  6
        'past_fraction_5f_9',               ##      914     NUMERIC         999.99  6
        'past_fraction_5f_10',              ##      915     NUMERIC         999.99  6

        'past_fraction_6f_1',               ##      916     NUMERIC         999.99  6
        'past_fraction_6f_2',               ##      917     NUMERIC         999.99  6
        'past_fraction_6f_3',               ##      918     NUMERIC         999.99  6
        'past_fraction_6f_4',               ##      919     NUMERIC         999.99  6
        'past_fraction_6f_5',               ##      920     NUMERIC         999.99  6
        'past_fraction_6f_6',               ##      921     NUMERIC         999.99  6
        'past_fraction_6f_7',               ##      922     NUMERIC         999.99  6
        'past_fraction_6f_8',               ##      923     NUMERIC         999.99  6
        'past_fraction_6f_9',               ##      924     NUMERIC         999.99  6
        'past_fraction_6f_10',              ##      925     NUMERIC         999.99  6

        'past_fraction_7f_1',               ##      926     NUMERIC         999.99  6
        'past_fraction_7f_2',               ##      927     NUMERIC         999.99  6
        'past_fraction_7f_3',               ##      928     NUMERIC         999.99  6
        'past_fraction_7f_4',               ##      929     NUMERIC         999.99  6
        'past_fraction_7f_5',               ##      930     NUMERIC         999.99  6
        'past_fraction_7f_6',               ##      931     NUMERIC         999.99  6
        'past_fraction_7f_7',               ##      932     NUMERIC         999.99  6
        'past_fraction_7f_8',               ##      933     NUMERIC         999.99  6
        'past_fraction_7f_9',               ##      934     NUMERIC         999.99  6
        'past_fraction_7f_10',              ##      935     NUMERIC         999.99  6

        'past_fraction_8f_1',               ##      936     NUMERIC         999.99  6
        'past_fraction_8f_2',               ##      937     NUMERIC         999.99  6
        'past_fraction_8f_3',               ##      938     NUMERIC         999.99  6
        'past_fraction_8f_4',               ##      939     NUMERIC         999.99  6
        'past_fraction_8f_5',               ##      940     NUMERIC         999.99  6
        'past_fraction_8f_6',               ##      941     NUMERIC         999.99  6
        'past_fraction_8f_7',               ##      942     NUMERIC         999.99  6
        'past_fraction_8f_8',               ##      943     NUMERIC         999.99  6
        'past_fraction_8f_9',               ##      944     NUMERIC         999.99  6
        'past_fraction_8f_10',              ##      945     NUMERIC         999.99  6

        'past_fraction_10f_1',              ##      946     NUMERIC         999.99  6
        'past_fraction_10f_2',              ##      947     NUMERIC         999.99  6
        'past_fraction_10f_3',              ##      948     NUMERIC         999.99  6
        'past_fraction_10f_4',              ##      949     NUMERIC         999.99  6
        'past_fraction_10f_5',              ##      950     NUMERIC         999.99  6
        'past_fraction_10f_6',              ##      951     NUMERIC         999.99  6
        'past_fraction_10f_7',              ##      952     NUMERIC         999.99  6
        'past_fraction_10f_8',              ##      953     NUMERIC         999.99  6
        'past_fraction_10f_9',              ##      954     NUMERIC         999.99  6
        'past_fraction_10f_10',             ##      955     NUMERIC         999.99  6

        'past_fraction_12f_1',              ##      956     NUMERIC         999.99  6
        'past_fraction_12f_2',              ##      957     NUMERIC         999.99  6
        'past_fraction_12f_3',              ##      958     NUMERIC         999.99  6
        'past_fraction_12f_4',              ##      959     NUMERIC         999.99  6
        'past_fraction_12f_5',              ##      960     NUMERIC         999.99  6
        'past_fraction_12f_6',              ##      961     NUMERIC         999.99  6
        'past_fraction_12f_7',              ##      962     NUMERIC         999.99  6
        'past_fraction_12f_8',              ##      963     NUMERIC         999.99  6
        'past_fraction_12f_9',              ##      964     NUMERIC         999.99  6
        'past_fraction_12f_10',             ##      965     NUMERIC         999.99  6

        'past_fraction_14f_1',              ##      966     NUMERIC         999.99  6
        'past_fraction_14f_2',              ##      967     NUMERIC         999.99  6
        'past_fraction_14f_3',              ##      968     NUMERIC         999.99  6
        'past_fraction_14f_4',              ##      969     NUMERIC         999.99  6
        'past_fraction_14f_5',              ##      970     NUMERIC         999.99  6
        'past_fraction_14f_6',              ##      971     NUMERIC         999.99  6
        'past_fraction_14f_7',              ##      972     NUMERIC         999.99  6
        'past_fraction_14f_8',              ##      973     NUMERIC         999.99  6
        'past_fraction_14f_9',              ##      974     NUMERIC         999.99  6
        'past_fraction_14f_10',             ##      975     NUMERIC         999.99  6

        'past_fraction_16f_1',              ##      976     NUMERIC         999.99  6
        'past_fraction_16f_2',              ##      977     NUMERIC         999.99  6
        'past_fraction_16f_3',              ##      978     NUMERIC         999.99  6
        'past_fraction_16f_4',              ##      979     NUMERIC         999.99  6
        'past_fraction_16f_5',              ##      980     NUMERIC         999.99  6
        'past_fraction_16f_6',              ##      981     NUMERIC         999.99  6
        'past_fraction_16f_7',              ##      982     NUMERIC         999.99  6
        'past_fraction_16f_8',              ##      983     NUMERIC         999.99  6
        'past_fraction_16f_9',              ##      984     NUMERIC         999.99  6
        'past_fraction_16f_10',             ##      985     NUMERIC         999.99  6

         ##     Fractions #1, #2, #3
        'past_fraction_first_1',            ##      986     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_first_2',            ##      987     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_first_3',            ##      988     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_first_4',            ##      989     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_first_5',            ##      990     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_first_6',            ##      991     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_first_7',            ##      992     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_first_8',            ##      993     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_first_9',            ##      994     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_first_10',           ##      995     NUMERIC         999.99  6       Seconds and hundreths

        'past_fraction_second_1',           ##      996     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_second_2',           ##      997     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_second_3',           ##      998     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_second_4',           ##      999     NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_second_5',           ##      1000    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_second_6',           ##      1001    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_second_7',           ##      1002    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_second_8',           ##      1003    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_second_9',           ##      1004    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_second_10',          ##      1005    NUMERIC         999.99  6       Seconds and hundreths

        'past_fraction_third_1',            ##      1006    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_third_2',            ##      1007    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_third_3',            ##      1008    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_third_4',            ##      1009    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_third_5',            ##      1010    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_third_6',            ##      1011    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_third_7',            ##      1012    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_third_8',            ##      1013    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_third_9',            ##      1014    NUMERIC         999.99  6       Seconds and hundreths
        'past_fraction_third_10',           ##      1015    NUMERIC         999.99  6       Seconds and hundreths

        'reserved1016',                     ##      1016
        'reserved1017',                     ##      1017
        'reserved1018',                     ##      1018
        'reserved1019',                     ##      1019
        'reserved1020',                     ##      1020
        'reserved1021',                     ##      1021
        'reserved1022',                     ##      1022
        'reserved1023',                     ##      1023
        'reserved1024',                     ##      1024
        'reserved1025',                     ##      1025
        'reserved1026',                     ##      1026
        'reserved1027',                     ##      1027
        'reserved1028',                     ##      1028
        'reserved1029',                     ##      1029
        'reserved1030',                     ##      1030
        'reserved1031',                     ##      1031
        'reserved1032',                     ##      1032
        'reserved1033',                     ##      1033
        'reserved1034',                     ##      1034
        'reserved1035',                     ##      1035

        ##      Final time
        'past_final_time_1',                ##      1036    NUMERIC         999.99  6       Seconds and hundreths
        'past_final_time_2',                ##      1037    NUMERIC         999.99  6
        'past_final_time_3',                ##      1038    NUMERIC         999.99  6
        'past_final_time_4',                ##      1039    NUMERIC         999.99  6
        'past_final_time_5',                ##      1040    NUMERIC         999.99  6
        'past_final_time_6',                ##      1041    NUMERIC         999.99  6
        'past_final_time_7',                ##      1042    NUMERIC         999.99  6
        'past_final_time_8',                ##      1043    NUMERIC         999.99  6
        'past_final_time_9',                ##      1044    NUMERIC         999.99  6
        'past_final_time_10',               ##      1045    NUMERIC         999.99  6

        ##      Claimed code
        'past_claimed_code_1',              ##      1046    CHARACTER       X       1       c- claimed
        'past_claimed_code_2',              ##      1047    CHARACTER       X       1
        'past_claimed_code_3',              ##      1048    CHARACTER       X       1
        'past_claimed_code_4',              ##      1049    CHARACTER       X       1
        'past_claimed_code_5',              ##      1050    CHARACTER       X       1
        'past_claimed_code_6',              ##      1051    CHARACTER       X       1
        'past_claimed_code_7',              ##      1052    CHARACTER       X       1
        'past_claimed_code_8',              ##      1053    CHARACTER       X       1
        'past_claimed_code_9',              ##      1054    CHARACTER       X       1
        'past_claimed_code_10',             ##      1055    CHARACTER       X       1

        ##      Past Trainer (when available) and Jockey
        'past_trainer_1',                   ##      1056    CHARACTER       X       30
        'past_trainer_2',                   ##      1057    CHARACTER       X       30
        'past_trainer_3',                   ##      1058    CHARACTER       X       30
        'past_trainer_4',                   ##      1059    CHARACTER       X       30
        'past_trainer_5',                   ##      1060    CHARACTER       X       30
        'past_trainer_6',                   ##      1061    CHARACTER       X       30
        'past_trainer_7',                   ##      1062    CHARACTER       X       30
        'past_trainer_8',                   ##      1063    CHARACTER       X       30
        'past_trainer_9',                   ##      1064    CHARACTER       X       30
        'past_trainer_10',                  ##      1065    CHARACTER       X       30

        'past_jockey_1',                    ##      1066    CHARACTER       X       30
        'past_jockey_2',                    ##      1067    CHARACTER       X       30
        'past_jockey_3',                    ##      1068    CHARACTER       X       30
        'past_jockey_4',                    ##      1069    CHARACTER       X       30
        'past_jockey_5',                    ##      1070    CHARACTER       X       30
        'past_jockey_6',                    ##      1071    CHARACTER       X       30
        'past_jockey_7',                    ##      1072    CHARACTER       X       30
        'past_jockey_8',                    ##      1073    CHARACTER       X       30
        'past_jockey_9',                    ##      1074    CHARACTER       X       30
        'past_jockey_10',                   ##      1075    CHARACTER       X       30

        ##      Apprentice weight allowance (if any)
        'past_weight_allowance_1',          ##      1076    NUMERIC         99      2
        'past_weight_allowance_2',          ##      1077    NUMERIC         99      2
        'past_weight_allowance_3',          ##      1078    NUMERIC         99      2
        'past_weight_allowance_4',          ##      1079    NUMERIC         99      2
        'past_weight_allowance_5',          ##      1080    NUMERIC         99      2
        'past_weight_allowance_6',          ##      1081    NUMERIC         99      2
        'past_weight_allowance_7',          ##      1082    NUMERIC         99      2
        'past_weight_allowance_8',          ##      1083    NUMERIC         99      2
        'past_weight_allowance_9',          ##      1084    NUMERIC         99      2
        'past_weight_allowance_10',         ##      1085    NUMERIC         99      2

        ##      Race type
        'past_race_type_1',                 ##      1086    CHARACTER       XX      2       (G1, G2, G3, N, A, R, T, C,
        'past_race_type_2',                 ##      1087    CHARACTER       XX      2       CO, S, M, AO, MO, NO)
        'past_race_type_3',                 ##      1088    CHARACTER       XX      2       See field #9
        'past_race_type_4',                 ##      1089    CHARACTER       XX      2
        'past_race_type_5',                 ##      1090    CHARACTER       XX      2
        'past_race_type_6',                 ##      1091    CHARACTER       XX      2       Age/Sex Restrictions
        'past_race_type_7',                 ##      1092    CHARACTER       XX      2       (3 character sting):
        'past_race_type_8',                 ##      1093    CHARACTER       XX      2       1st character:
        'past_race_type_9',                 ##      1094    CHARACTER       XX      2       A- 2 year olds
        'past_race_type_10',                ##      1095    CHARACTER       XX      2       B- 3 year olds
                                            ##                                              C- 4 year olds
        ##      Age and sex restrictions                                                    D- 5 year olds
        'past_age_sex_restrictions_1',      ##      1096    CHARACTER       XXX     3       E- 3 & 4 year olds
        'past_age_sex_restrictions_2',      ##      1097    CHARACTER       XXX     3       F- 4 & 5 year olds
        'past_age_sex_restrictions_3',      ##      1098    CHARACTER       XXX     3       G- 3, 4, & 5 year olds
        'past_age_sex_restrictions_4',      ##      1099    CHARACTER       XXX     3       H- all ages
        'past_age_sex_restrictions_5',      ##      1100    CHARACTER       XXX     3
        'past_age_sex_restrictions_6',      ##      1101    CHARACTER       XXX     3       2d Character:
        'past_age_sex_restrictions_7',      ##      1102    CHARACTER       XXX     3       O- That age only
        'past_age_sex_restrictions_8',      ##      1103    CHARACTER       XXX     3       U- That age and up
        'past_age_sex_restrictions_9',      ##      1104    CHARACTER       XXX     3
        'past_age_sex_restrictions_10',     ##      1105    CHARACTER       XXX     3       3d character
                                            ##                                              N - No Sex Restrictions
                                            ##                                              M - Mares and Fillies Only
                                            ##                                              C - Colts or Geldings Only
                                            ##                                              F - Fillies Only
                                            ##      E.g.: 'BON' - means a '3 year olds only,'  no sex restrictions

        ##      Statebred flag
        'past_statebred_flag_1',            ##      1106    CHARACTER       X       1       s- Statebred
        'past_statebred_flag_2',            ##      1107    CHARACTER       X       1
        'past_statebred_flag_3',            ##      1108    CHARACTER       X       1
        'past_statebred_flag_4',            ##      1109    CHARACTER       X       1
        'past_statebred_flag_5',            ##      1110    CHARACTER       X       1
        'past_statebred_flag_6',            ##      1111    CHARACTER       X       1
        'past_statebred_flag_7',            ##      1112    CHARACTER       X       1
        'past_statebred_flag_8',            ##      1113    CHARACTER       X       1
        'past_statebred_flag_9',            ##      1114    CHARACTER       X       1
        'past_statebred_flag_10',           ##      1115    CHARACTER       X       1

        ##      Restricted/Qualified flag
        'past_restricted_or_qualified_1',   ##      1116    CHARACTER       X       R- restrcited
        'past_restricted_or_qualified_2',   ##      1117    CHARACTER       X       Q- Qualifier
        'past_restricted_or_qualified_3',   ##      1118    CHARACTER       X       O- Optional claimer
        'past_restricted_or_qualified_4',   ##      1119    CHARACTER       X
        'past_restricted_or_qualified_5',   ##      1120    CHARACTER       X
        'past_restricted_or_qualified_6',   ##      1121    CHARACTER       X
        'past_restricted_or_qualified_7',   ##      1122    CHARACTER       X
        'past_restricted_or_qualified_8',   ##      1123    CHARACTER       X
        'past_restricted_or_qualified_9',   ##      1124    CHARACTER       X
        'past_restricted_or_qualified_10',  ##      1125    CHARACTER       X

        ##      Favorite indicator
        'past_favorite_flag_1',             ##      1126    NUMERIC         X       0- Non-favorite
        'past_favorite_flag_2',             ##      1127    NUMERIC         X       1- Favorite
        'past_favorite_flag_3',             ##      1128    NUMERIC         X
        'past_favorite_flag_4',             ##      1129    NUMERIC         X
        'past_favorite_flag_5',             ##      1130    NUMERIC         X
        'past_favorite_flag_6',             ##      1131    NUMERIC         X
        'past_favorite_flag_7',             ##      1132    NUMERIC         X
        'past_favorite_flag_8',             ##      1133    NUMERIC         X
        'past_favorite_flag_9',             ##      1134    NUMERIC         X
        'past_favorite_flag_10',            ##      1135    NUMERIC         X

        ##      Front bandages indicator
        'past_front_wraps_1',               ##      1136    NUMERIC         X       0- No front wraps
        'past_front_wraps_2',               ##      1137    NUMERIC         X       1- Front wraps
        'past_front_wraps_3',               ##      1138    NUMERIC         X
        'past_front_wraps_4',               ##      1139    NUMERIC         X
        'past_front_wraps_5',               ##      1140    NUMERIC         X
        'past_front_wraps_6',               ##      1141    NUMERIC         X
        'past_front_wraps_7',               ##      1142    NUMERIC         X
        'past_front_wraps_8',               ##      1143    NUMERIC         X
        'past_front_wraps_9',               ##      1144    NUMERIC         X
        'past_front_wraps_10',              ##      1145    NUMERIC         X

        'reserved1146',                     ##      1146

        ##      Trainer and Jockey stats Current/Past Year
        'trainer_current_year_starts',      ##      1147    NUMERIC         9999    4
        'trainer_current_year_wins',        ##      1148
        'trainer_current_year_places',      ##      1149
        'trainer_current_year_shows',       ##      1150
        'trainer_current_year_roi',         ##      1151    NUMERIC         999.99  6
        'trainer_past_year_starts',         ##      1152    NUMERIC         9999    4
        'trainer_past_year_wins',           ##      1153
        'trainer_past_year_places',         ##      1154
        'trainer_past_year_shows',          ##      1155
        'trainer_past_year_roi',            ##      1156    NUMERIC         999.99  6
        'jockey_current_year_starts',       ##      1157    NUMERIC         9999    4
        'jockey_current_year_wins',         ##      1158    NUMERIC
        'jockey_current_year_places',       ##      1159    NUMERIC
        'jockey_current_year_shows',        ##      1160    NUMERIC
        'jockey_current_year_roi',          ##      1161    NUMERIC         999.99  6
        'jockey_past_year_starts',          ##      1162    NUMERIC         9999    4
        'jockey_past_year_wins',            ##      1163    NUMERIC
        'jockey_past_year_places',          ##      1164    NUMERIC
        'jockey_past_year_shows',           ##      1165    NUMERIC
        'jockey_past_year_roi',             ##      1166    NUMERIC         999.99  6

        ##      BRIS Speed Par for Class Level of last 10 races
        'past_bris_par_for_class_1',        ##      1167                            3
        'past_bris_par_for_class_2',        ##      1168                            3
        'past_bris_par_for_class_3',        ##      1169                            3
        'past_bris_par_for_class_4',        ##      1170                            3
        'past_bris_par_for_class_5',        ##      1171                            3
        'past_bris_par_for_class_6',        ##      1172                            3
        'past_bris_par_for_class_7',        ##      1173                            3
        'past_bris_par_for_class_8',        ##      1174                            3
        'past_bris_par_for_class_9',        ##      1175                            3
        'past_bris_par_for_class_10',       ##      1176                            3

        ##      Sire stud fee (current)
        'sire_stud_fee_current',            ##      1177    NUMERIC         9999999 7

        ##      Best BRIS Speeds
        'best_bris_speed_fast',             ##      1178    NUMERIC         999     3
        'best_bris_speed_turf',             ##      1179    NUMERIC         999     3
        'best_bris_speed_off_track',        ##      1180    NUMERIC         999     3
        'best_bris_speed_at_distance',     ##      1181    NUMERIC         999     3

        ## Bar Shoe WHAT DOES THIS MEAN?
        'past_bar_shoe_1',                  ##      1182    CHARACTER       X       1       r- bar shoe
        'past_bar_shoe_2',                  ##      1183    CHARACTER       X       1
        'past_bar_shoe_3',                  ##      1184    CHARACTER       X       1
        'past_bar_shoe_4',                  ##      1185    CHARACTER       X       1
        'past_bar_shoe_5',                  ##      1186    CHARACTER       X       1
        'past_bar_shoe_6',                  ##      1187    CHARACTER       X       1
        'past_bar_shoe_7',                  ##      1188    CHARACTER       X       1
        'past_bar_shoe_8',                  ##      1189    CHARACTER       X       1
        'past_bar_shoe_9',                  ##      1190    CHARACTER       X       1
        'past_bar_shoe_10',                 ##      1191    CHARACTER       X       1

        ##      Company line codes
        'past_company_line_1',              ##      1192    CHARACTER       XXXX    4
        'past_company_line_2',              ##      1193    CHARACTER       XXXX    4
        'past_company_line_3',              ##      1194    CHARACTER       XXXX    4
        'past_company_line_4',              ##      1195    CHARACTER       XXXX    4
        'past_company_line_5',              ##      1196    CHARACTER       XXXX    4
        'past_company_line_6',              ##      1197    CHARACTER       XXXX    4
        'past_company_line_7',              ##      1198    CHARACTER       XXXX    4
        'past_company_line_8',              ##      1199    CHARACTER       XXXX    4
        'past_company_line_9',              ##      1200    CHARACTER       XXXX    4
        'past_company_line_10',             ##      1201    CHARACTER       XXXX    4

        ##      High and Low claiming price of race
        'past_low_claiming_price_1',        ##      1202    NUMERIC         9999999 7
        'past_low_claiming_price_2',        ##      1203    NUMERIC         9999999 7
        'past_low_claiming_price_3',        ##      1204    NUMERIC         9999999 7
        'past_low_claiming_price_4',        ##      1205    NUMERIC         9999999 7
        'past_low_claiming_price_5',        ##      1206    NUMERIC         9999999 7
        'past_low_claiming_price_6',        ##      1207    NUMERIC         9999999 7
        'past_low_claiming_price_7',        ##      1208    NUMERIC         9999999 7
        'past_low_claiming_price_8',        ##      1209    NUMERIC         9999999 7
        'past_low_claiming_price_9',        ##      1210    NUMERIC         9999999 7
        'past_low_claiming_price_10',       ##      1211    NUMERIC         9999999 7

        'past_high_claiming_price_1',       ##      1212    NUMERIC         9999999 7
        'past_high_claiming_price_2',       ##      1213    NUMERIC         9999999 7
        'past_high_claiming_price_3',       ##      1214    NUMERIC         9999999 7
        'past_high_claiming_price_4',       ##      1215    NUMERIC         9999999 7
        'past_high_claiming_price_5',       ##      1216    NUMERIC         9999999 7
        'past_high_claiming_price_6',       ##      1217    NUMERIC         9999999 7
        'past_high_claiming_price_7',       ##      1218    NUMERIC         9999999 7
        'past_high_claiming_price_8',       ##      1219    NUMERIC         9999999 7
        'past_high_claiming_price_9',       ##      1220    NUMERIC         9999999 7
        'past_high_claiming_price_10',      ##      1221    NUMERIC         9999999 7

        ##      Aution price and when/when sold at auction
        'auction_price',                    ##      1222    NUMERIC         999999999       9
        'auction_where_when',               ##      1223    CHARACTER       X(12)           12

        ##      reserved for future use
        'reserved1224',                     ##      1224
        'reserved1225',                     ##      1225
        'reserved1226',                     ##      1226
        'reserved1227',                     ##      1227
        'reserved1228',                     ##      1228
        'reserved1229',                     ##      1229
        'reserved1230',                     ##      1230
        'reserved1231',                     ##      1231
        'reserved1232',                     ##      1232
        'reserved1233',                     ##      1233
        'reserved1234',                     ##      1234
        'reserved1235',                     ##      1235
        'reserved1236',                     ##      1236
        'reserved1237',                     ##      1237
        'reserved1238',                     ##      1238
        'reserved1239',                     ##      1239
        'reserved1240',                     ##      1240
        'reserved1241',                     ##      1241
        'reserved1242',                     ##      1242
        'reserved1243',                     ##      1243
        'reserved1244',                     ##      1244
        'reserved1245',                     ##      1245
        'reserved1246',                     ##      1246
        'reserved1247',                     ##      1247
        'reserved1248',                     ##      1248
        'reserved1249',                     ##      1249
        'reserved1250',                     ##      1250
        'reserved1251',                     ##      1251
        'reserved1252',                     ##      1252
        'reserved1253',                     ##      1253

        ##      Code for prior 10 starts
        'past_start_code_1',                ##      1254                                    1       's'- Nasal strip
        'past_start_code_2',                ##      1255                                    1       'x'- Off the turf
        'past_start_code_3',                ##      1256                                    1
        'past_start_code_4',                ##      1257                                    1
        'past_start_code_5',                ##      1258                                    1
        'past_start_code_6',                ##      1259                                    1
        'past_start_code_7',                ##      1260                                    1
        'past_start_code_8',                ##      1261                                    1
        'past_start_code_9',                ##      1262                                    1
        'past_start_code_10',               ##      1263                                    1

        ##      BRIS Pedigree Ratings
        'bris_pedigree_rating_dirt',        ##      1264    CHARACTER       XXXX    4       e.g., '115'
        'bris_pedigree_rating_mud',         ##      1265    CHARACTER       XXXX    4
        'bris_pedigree_rating_turf',        ##      1266    CHARACTER       XXXX    4
        'bris_pedigree_rating_at_distance', ##      1267    CHARACTER       XXXX    4

        ##      Claimed from and trainer siwtches
        'past_claim_trainer_switch_date_1', ##      1268    CHARACTER               10      e.g. '12/30/2000'
        'past_claim_trainer_switch_date_2', ##      1269    CHARACTER               10
        'past_claim_trainer_switch_date_3', ##      1270    CHARACTER               10
        'past_claim_trainer_switch_date_4', ##      1271    CHARACTER               10
        'past_claim_trainer_switch_date_5', ##      1272    CHARACTER               10
        'past_claim_trainer_switch_date_6', ##      1273    CHARACTER               10
        'past_claim_trainer_switch_date_7', ##      1274    CHARACTER               10
        'past_claim_trainer_switch_date_8', ##      1275    CHARACTER               10
        'past_claim_trainer_switch_date_9', ##      1276    CHARACTER               10
        'past_claim_trainer_switch_date_10',##      1277    CHARACTER               10

        ##      Claimed from and trainer switches
        'past_claim_trainer_switch_1_1',    ##      1278    NUMERIC                 4
        'past_claim_trainer_switch_1_2',    ##      1279    NUMERIC                 4
        'past_claim_trainer_switch_1_3',    ##      1280    NUMERIC                 4
        'past_claim_trainer_switch_1_4',    ##      1281    NUMERIC                 4
        'past_claim_trainer_switch_1_5',    ##      1282    NUMERIC                 4
        'past_claim_trainer_switch_1_6',    ##      1283    NUMERIC                 4
        'past_claim_trainer_switch_1_7',    ##      1284    NUMERIC                 4
        'past_claim_trainer_switch_1_8',    ##      1285    NUMERIC                 4
        'past_claim_trainer_switch_1_9',    ##      1286    NUMERIC                 4
        'past_claim_trainer_switch_1_10',   ##      1287    NUMERIC                 4

        ##      Claimed from and trainer switches
        'past_claim_trainer_switch_2_1',    ##      1288    NUMERIC                 4
        'past_claim_trainer_switch_2_2',    ##      1289    NUMERIC                 4
        'past_claim_trainer_switch_2_3',    ##      1290    NUMERIC                 4
        'past_claim_trainer_switch_2_4',    ##      1291    NUMERIC                 4
        'past_claim_trainer_switch_2_5',    ##      1292    NUMERIC                 4
        'past_claim_trainer_switch_2_6',    ##      1293    NUMERIC                 4
        'past_claim_trainer_switch_2_7',    ##      1294    NUMERIC                 4
        'past_claim_trainer_switch_2_8',    ##      1295    NUMERIC                 4
        'past_claim_trainer_switch_2_9',    ##      1296    NUMERIC                 4
        'past_claim_trainer_switch_2_10',   ##      1297    NUMERIC                 4

        ##      Claimed from and trainer switches
        'past_claim_trainer_switch_3_1',    ##      1298    NUMERIC                 4
        'past_claim_trainer_switch_3_2',    ##      1299    NUMERIC                 4
        'past_claim_trainer_switch_3_3',    ##      1300    NUMERIC                 4
        'past_claim_trainer_switch_3_4',    ##      1301    NUMERIC                 4
        'past_claim_trainer_switch_3_5',    ##      1302    NUMERIC                 4
        'past_claim_trainer_switch_3_6',    ##      1303    NUMERIC                 4
        'past_claim_trainer_switch_3_7',    ##      1304    NUMERIC                 4
        'past_claim_trainer_switch_3_8',    ##      1305    NUMERIC                 4
        'past_claim_trainer_switch_3_9',    ##      1306    NUMERIC                 4
        'past_claim_trainer_switch_3_10',   ##      1307    NUMERIC                 4

        ##      Claimed from and trainer switches
        'past_claim_trainer_switch_4_1',    ##      1308    NUMERIC                 4
        'past_claim_trainer_switch_4_2',    ##      1309    NUMERIC                 4
        'past_claim_trainer_switch_4_3',    ##      1310    NUMERIC                 4
        'past_claim_trainer_switch_4_4',    ##      1311    NUMERIC                 4
        'past_claim_trainer_switch_4_5',    ##      1312    NUMERIC                 4
        'past_claim_trainer_switch_4_6',    ##      1313    NUMERIC                 4
        'past_claim_trainer_switch_4_7',    ##      1314    NUMERIC                 4
        'past_claim_trainer_switch_4_8',    ##      1315    NUMERIC                 4
        'past_claim_trainer_switch_4_9',    ##      1316    NUMERIC                 4
        'past_claim_trainer_switch_4_10',   ##      1317    NUMERIC                 4

        ##      Claimed from and trainer switches
        'past_claim_trainer_switch_5_1',    ##      1318    NUMERIC                 4
        'past_claim_trainer_switch_5_2',    ##      1319    NUMERIC                 4
        'past_claim_trainer_switch_5_3',    ##      1320    NUMERIC                 4
        'past_claim_trainer_switch_5_4',    ##      1321    NUMERIC                 4
        'past_claim_trainer_switch_5_5',    ##      1322    NUMERIC                 4
        'past_claim_trainer_switch_5_6',    ##      1323    NUMERIC                 4
        'past_claim_trainer_switch_5_7',    ##      1324    NUMERIC                 4
        'past_claim_trainer_switch_5_8',    ##      1325    NUMERIC                 4
        'past_claim_trainer_switch_5_9',    ##      1326    NUMERIC                 4
        'past_claim_trainer_switch_5_10',   ##      1327    NUMERIC                 4


        ##      Best BRIS Speeds: Life, Most recent year horse ran, 2d most recent year horse ran, today's track
        'best_bris_speed_life',             ##      1328    NUMERIC         9999    4
        'best_bris_speed_recent_year',      ##      1329    NUMERIC         9999    4
        'best_bris_speed_2d_recent_year',   ##      1330    NUMERIC         9999    4
        'best_bris_speed_todays_track',     ##      1331    NUMERIC         9999    4

        ##      Fast Dirt stats
        'fast_dirt_starts',                 ##      1332    NUMERIC         999     3
        'fast_dirt_wins',                   ##      1333    NUMERIC         99      2
        'fast_dirt_places',                 ##      1334    NUMERIC         99      2
        'fast_dirt_shows',             ##      1335    NUMERIC         99      2
        'fast_dirt_earned',               ##      1336    NUMERIC         9(9)    9

        ## Key Traininer stat Category 1

        'trainer_stat_1_name',              ##      1337    CHARACTER       X(16)   16
        'trainer_stat_1_starts',            ##      1338    NUMERIC         9999    4
        'trainer_stat_1_win_percent',       ##      1339    NUMERIC         999.99  6
        'trainer_stat_1_itm_percent',       ##      1340    NUMERIC         999.99  6       In the money percentage
        'trainer_stat_1_roi',               ##      1341    NUMERIC         999.99  6       $2 return on investment

        ## Key Traininer stat Category 2

        'trainer_stat_2_name',              ##      1342    CHARACTER       X(16)   16
        'trainer_stat_2_starts',            ##      1343    NUMERIC         9999    4
        'trainer_stat_2_win_percent',       ##      1344    NUMERIC         999.99  6
        'trainer_stat_2_itm_percent',       ##      1345    NUMERIC         999.99  6       In the money percentage
        'trainer_stat_2_roi',               ##      1346    NUMERIC         999.99  6       $2 return on investment

        ## Key Traininer stat Category 3

        'trainer_stat_3_name',              ##      1347    CHARACTER       X(16)   16
        'trainer_stat_3_starts',            ##      1348    NUMERIC         9999    4
        'trainer_stat_3_win_percent',       ##      1349    NUMERIC         999.99  6
        'trainer_stat_3_itm_percent',       ##      1350    NUMERIC         999.99  6       In the money percentage
        'trainer_stat_3_roi',               ##      1351    NUMERIC         999.99  6       $2 return on investment

        ## Key Traininer stat Category 4

        'trainer_stat_4_name',              ##      1352    CHARACTER       X(16)   16
        'trainer_stat_4_starts',            ##      1353    NUMERIC         9999    4
        'trainer_stat_4_win_percent',       ##      1354    NUMERIC         999.99  6
        'trainer_stat_4_itm_percent',       ##      1355    NUMERIC         999.99  6       In the money percentage
        'trainer_stat_4_roi',               ##      1356    NUMERIC         999.99  6       $2 return on investment

        ## Key Traininer stat Category 5

        'trainer_stat_5_name',              ##      1357    CHARACTER       X(16)   16
        'trainer_stat_5_starts',            ##      1358    NUMERIC         9999    4
        'trainer_stat_5_win_percent',       ##      1359    NUMERIC         999.99  6
        'trainer_stat_5_itm_percent',       ##      1360    NUMERIC         999.99  6       In the money percentage
        'trainer_stat_5_roi',               ##      1361    NUMERIC         999.99  6       $2 return on investment

        ## Key Traininer stat Category 6

        'trainer_stat_6_name',              ##      1362    CHARACTER       X(16)   16
        'trainer_stat_6_starts',            ##      1363    NUMERIC         9999    4
        'trainer_stat_6_win_percent',       ##      1364    NUMERIC         999.99  6
        'trainer_stat_6_itm_percent',       ##      1365    NUMERIC         999.99  6       In the money percentage
        'trainer_stat_6_roi',               ##      1366    NUMERIC         999.99  6       $2 return on investment

        ##      JKY @ Distance/ Jky on Turf stats

        'jockey_at_distance_on_turf_label',     ##      1367    CHARACTER       X(13)   13
        'jockey_at_distance_on_turf_starts',    ##      1368    NUMERIC         9999    4
        'jockey_at_distance_on_turf_wins',      ##      1369    NUMERIC         9999    4
        'jockey_at_distance_on_turf_places',    ##      1370    NUMERIC         9999    4
        'jockey_at_distance_on_turf_shows',     ##      1371    NUMERIC         9999    4
        'jockey_at_distance_on_turf_roi',       ##      1372    NUMERIC         999.99  6
        'jockey_at_distance_on_turf_earnings',  ##      1373    NUMERIC         9(8)    8

        ## Post times(by region)

        'post_times_by_region',             ##      1374    CHARACTER       X(50)   50

        ##      reserved
        'reserved1375',                     ##      1375
        'reserved1376',                     ##      1376
        'reserved1377',                     ##      1377
        'reserved1378',                     ##      1378
        'reserved1379',                     ##      1379
        'reserved1380',                     ##      1380
        'reserved1381',                     ##      1381
        'reserved1382',                     ##      1382

        ##      Extended Start Comment
        'past_extended_start_comment_1',    ##      1383    CHARACTER       X(90)   90
        'past_extended_start_comment_2',    ##      1384    CHARACTER       X(90)   90
        'past_extended_start_comment_3',    ##      1385    CHARACTER       X(90)   90
        'past_extended_start_comment_4',    ##      1386    CHARACTER       X(90)   90
        'past_extended_start_comment_5',    ##      1387    CHARACTER       X(90)   90
        'past_extended_start_comment_6',    ##      1388    CHARACTER       X(90)   90
        'past_extended_start_comment_7',    ##      1389    CHARACTER       X(90)   90
        'past_extended_start_comment_8',    ##      1390    CHARACTER       X(90)   90
        'past_extended_start_comment_9',    ##      1391    CHARACTER       X(90)   90
        'past_extended_start_comment_10',   ##      1392    CHARACTER       X(90)   90

        ##      'Sealed' track indicator
        'past_sealed_track_indicator_1',    ##      1393    CHARACTER       X       1       's'- Sealed
        'past_sealed_track_indicator_2',    ##      1394    CHARACTER       X       1
        'past_sealed_track_indicator_3',    ##      1395    CHARACTER       X       1
        'past_sealed_track_indicator_4',    ##      1396    CHARACTER       X       1
        'past_sealed_track_indicator_5',    ##      1397    CHARACTER       X       1
        'past_sealed_track_indicator_6',    ##      1398    CHARACTER       X       1
        'past_sealed_track_indicator_7',    ##      1399    CHARACTER       X       1
        'past_sealed_track_indicator_8',    ##      1400    CHARACTER       X       1
        'past_sealed_track_indicator_9',    ##      1401    CHARACTER       X       1
        'past_sealed_track_indicator_10',   ##      1402    CHARACTER       X       1

        ##      Prev. All-Weather Sureface Flag
        'past_all_weather_flag_1',          ##      1403    CHARACTER       X       1       A- All weather surface
        'past_all_weather_flag_2',          ##      1404    CHARACTER       X       1
        'past_all_weather_flag_3',          ##      1405    CHARACTER       X       1
        'past_all_weather_flag_4',          ##      1406    CHARACTER       X       1
        'past_all_weather_flag_5',          ##      1407    CHARACTER       X       1
        'past_all_weather_flag_6',          ##      1408    CHARACTER       X       1
        'past_all_weather_flag_7',          ##      1409    CHARACTER       X       1
        'past_all_weather_flag_8',          ##      1410    CHARACTER       X       1
        'past_all_weather_flag_9',          ##      1411    CHARACTER       X       1
        'past_all_weather_flag_10',         ##      1412    CHARACTER       X       1

        ##      Trainer/Jockey combo stats (meet)
        'TJ_combo_starts',                  ##      1413    NUMERIC         9999    4
        'TJ_combo_wins',                    ##      1414    NUMERIC         9999    4
        'TJ_combo_places',                  ##      1415    NUMERIC         9999    4
        'TJ_combo_shows',                   ##      1416    NUMERIC         9999    4
        'TJ_combo_roi',                     ##      1417    NUMERIC         999.99  6       $2 return on investment

        ##      Post time (PAcific military time) '0300' for 3am pacific time
        'post_time_pacific_military',          ##      1418    CHARACTER       XXXX    4

        ##      Equibase abbreviated race conditions
        'past_equibase_race_conditions_1',  ##      1419    CHARACTER       X(17)   17
        'past_equibase_race_conditions_2',  ##      1420    CHARACTER       X(17)   17
        'past_equibase_race_conditions_3',  ##      1421    CHARACTER       X(17)   17
        'past_equibase_race_conditions_4',  ##      1421    CHARACTER       X(17)   17
        'past_equibase_race_conditions_5',  ##      1423    CHARACTER       X(17)   17
        'past_equibase_race_conditions_6',  ##      1424    CHARACTER       X(17)   17
        'past_equibase_race_conditions_7',  ##      1425    CHARACTER       X(17)   17
        'past_equibase_race_conditions_8',  ##      1426    CHARACTER       X(17)   17
        'past_equibase_race_conditions_9',  ##      1427    CHARACTER       X(17)   17
        'past_equibase_race_conditions_10', ##      1428    CHARACTER       X(17)   17

        ##      Today's EQuibase abbreviated race conditions

        'equibase_race_conditions',         ##      1429    CHARACTER       X(17)   17

        ##      1430 - 1435  	Reserved
        'reserved1430',                     ##      1430
        'reserved1431',                     ##      1431
        'reserved1432',                     ##      1432
        'reserved1433',                     ##      1433
        'reserved1434',                     ##      1434
        'reserved1435'                      ##      1435
    ],
}

file_dtypes = {
    '1': {
        'track_code': 'VARCHAR(255)',
        'date': 'DATE',
        'race_num': 'INT',
        'day_evening_flag': 'VARCHAR(255)',
        'distance': 'FLOAT',
        'distance_units': 'VARCHAR(255)',
        'about_dist_flag': 'INT',
        'surface_old_style': 'VARCHAR(255)',
        'surface_new_style': 'VARCHAR(255)',
        'all_weather_flag': 'INT',
        'chute_start_flag': 'INT',
        'BRIS_race_type': 'VARCHAR(255)',
        'equibase_race_type': 'VARCHAR(255)',
        'race_grade': 'INT',
        'age_sex_restrictions': 'VARCHAR(255)',
        'race_restrict_code': 'VARCHAR(255)',
        'state_bred_flag': 'INT',
        'abbrev_race_class': 'VARCHAR(255)',
        'breed_of_race': 'VARCHAR(255)',
        'country_code': 'VARCHAR(255)',
        'purse': 'INT',
        'total_race_value': 'INT',
        'max_claim_price': 'INT',
        'race_conditions_1': 'VARCHAR(255)',
        'race_conditions_2': 'VARCHAR(255)',
        'race_conditions_3': 'VARCHAR(255)',
        'race_conditions_4': 'VARCHAR(255)',
        'race_conditions_5': 'VARCHAR(255)',
        'field_size': 'INT',
        'track_condition': 'VARCHAR(255)',
        'fraction_1_time': 'FLOAT',
        'fraction_2_time': 'FLOAT',
        'fraction_3_time': 'FLOAT',
        'fraction_4_time': 'FLOAT',
        'fraction_5_time': 'FLOAT',
        'final_time': 'FLOAT',
        'fraction_1_dist': 'INT',
        'fraction_2_dist': 'INT',
        'fraction_3_dist': 'INT',
        'fraction_4_dist': 'INT',
        'fraction_5_dist': 'INT',
        'off_time': 'INT',
        'start_call_dist': 'INT',
        'call_dist_first': 'INT',
        'call_dist_second': 'INT',
        'call_dist_third': 'INT',
        'race_name': 'VARCHAR(255)',
        'start_description': 'VARCHAR(255)',
        'temp_rail_dist': 'INT',
        'off_turf_flag': 'INT',
        'off_turf_dist_change': 'INT',
        'weather': 'VARCHAR(255)',
        'race_temp': 'INT',
        'WPS_show_pool': 'FLOAT',
        'run_up_dist': 'INT',
    },

    '2': {
        'track_code': 'VARCHAR(255)',
        'date': 'DATE',
        'race_num': 'INT',
        'day_evening_flag': 'VARCHAR(255)',
        'horse_name': 'VARCHAR(255)',
        'foreign_bred_code': 'VARCHAR(255)',
        'state_bred_code': 'VARCHAR(255)',
        'post_position': 'INT',
        'program_number': 'VARCHAR(255)',
        'birth_year': 'INT',
        'breed': 'VARCHAR(255)',
        'coupled_flag': 'VARCHAR(255)',
        'jockey_name': 'VARCHAR(255)',
        'jockey_last_name': 'VARCHAR(255)',
        'jockey_first_name': 'VARCHAR(255)',
        'jockey_middle_name': 'VARCHAR(255)',
        'trainer_name': 'VARCHAR(255)',
        'trainer_last_name': 'VARCHAR(255)',
        'trainer_first_name': 'VARCHAR(255)',
        'trainer_middle_name': 'VARCHAR(255)',
        'trip_comment': 'VARCHAR(255)',
        'owner_name': 'VARCHAR(255)',
        'owner_first_name': 'VARCHAR(255)',
        'owner_middle_name': 'VARCHAR(255)',
        'claiming_price': 'INT',
        'medication_codes': 'VARCHAR(255)',
        'equipment_code': 'VARCHAR(255)',
        'earnings': 'INT',
        'odds': 'FLOAT',
        'nonbetting_flag': 'INT',
        'favorite_flag': 'INT',
        'disqualified_flag': 'INT',
        'disqualified_placing': 'INT',
        'weight': 'INT',
        'corrected_weight': 'INT',
        'overweight_amt': 'INT',
        'claimed_flag': 'INT',
        'claimed_trainer': 'VARCHAR(255)',
        'claimed_trainer_last': 'VARCHAR(255)',
        'claimed_trainer_first': 'VARCHAR(255)',
        'claimed_trainer_middle': 'VARCHAR(255)',
        'claimed_owner': 'VARCHAR(255)',
        'claimed_owner_last': 'VARCHAR(255)',
        'claimed_owner_first': 'VARCHAR(255)',
        'claimed_owner_middle': 'VARCHAR(255)',
        'win_payout': 'FLOAT',
        'place_payout': 'FLOAT',
        'show_payout': 'FLOAT',
        'start_call_pos': 'INT',
        '1st_call_pos': 'INT',
        '2d_call_pos': 'INT',
        '3d_call_pos': 'INT',
        'stretch_call_pos': 'INT',
        'finish_pos': 'INT',
        'official_finish_pos': 'INT',
        'start_lead': 'FLOAT',
        '1st_call_lead': 'FLOAT',
        '2d_call_lead': 'FLOAT',
        '3d_call_lead': 'FLOAT',
        'stretch_call_lead': 'FLOAT',
        'finish_lead': 'FLOAT',
        'start_beaten': 'FLOAT',
        '1st_call_beaten': 'FLOAT',
        '2d_call_beaten': 'FLOAT',
        '3d_call_beaten': 'FLOAT',
        'stretch_call_beaten': 'FLOAT',
        'finish_beaten': 'FLOAT',
        'lead_or_beaten_lengths_start': 'FLOAT',
        'lead_or_beaten_lengths_1st_call': 'FLOAT',
        'lead_or_beaten_lengths_2d_call': 'FLOAT',
        'lead_or_beaten_lengths_3d_call': 'FLOAT',
        'lead_or_beaten_lengths_stretch_call': 'FLOAT',
        'lead_or_beaten_lengths_finish': 'FLOAT',

        'start_margin': 'FLOAT',
        '1st_call_margin': 'FLOAT',
        '2d_call_margin': 'FLOAT',
        '3d_call_margin': 'FLOAT',
        'stretch_call_margin': 'FLOAT',
        'finish_margin': 'FLOAT',
        'dead_heat_flag': 'INT',
        'horse_reg_id': 'VARCHAR(255)',
        'jockey_id': 'INT',
        'trainer_id': 'INT',
        'owner_id': 'INT',
        'claimed_trainer_id': 'INT',
        'claimed_owner_id': 'INT',

        # Added features:
        'meds_adjunct_bleeder': 'INT',
        'meds_bute': 'INT',
        'meds_lasix': 'INT',

        'running_ws': 'INT',
        'screens': 'INT',
        'shields': 'INT',
        'aluminum_pads': 'INT',
        'blinkers': 'INT',
        'mud_calks': 'INT',
        'glued_shoes': 'INT',
        'inner_rims': 'INT',
        'front_bandages': 'INT',
        'goggles': 'INT',
        'outer_rims': 'INT',
        'inserts': 'INT',
        'aluminum_pad': 'INT',
        'flipping_halter': 'INT',
        'bar_shoes': 'INT',
        'blocks': 'INT',
        'no_whip': 'INT',
        'blinkers_off': 'INT',
        'pads': 'INT',
        'nasal_strip_off': 'INT',
        'bar_shoe': 'INT',
        'nasal_strip': 'INT',
        'turndowns': 'INT',
        'spurs': 'INT',
        'cheek_piece': 'INT',
        'queens_plates': 'INT',
        'cheek_piece_off': 'INT',
        'no_shoes': 'INT',
        'tongue_tie': 'INT',
    },

    '3': {
        'track_code': 'VARCHAR(255)',
        'date': 'DATE',
        'race_num': 'INT',
        'day_evening_flag': 'VARCHAR(255)',
        'horse_name': 'VARCHAR(255)',
        'foreign_bred_code': 'VARCHAR(255)',
        'statebred_code': 'VARCHAR(255)',
        'program_number': 'VARCHAR(255)',
        'win_payout': 'FLOAT',
        'place_payout': 'FLOAT',
        'show_payout': 'FLOAT',
    },

    '4': {
        'track_code': 'VARCHAR(255)',
        'date': 'DATE',
        'race_num': 'INT',
        'day_evening_flag': 'VARCHAR(255)',
        'wager_type': 'VARCHAR(255)',
        'bet_amount': 'FLOAT',
        'payout_amount': 'FLOAT',
        'number_correct': 'VARCHAR(255)',
        'winning_numbers': 'VARCHAR(255)',
        'wager_pool': 'FLOAT',
        'carryover_amount': 'FLOAT'
    },

    '5': {
        'track_code': 'VARCHAR(255)',
        'date': 'DATE',
        'race_num': 'INT',
        'day_evening_flag': 'VARCHAR(255)',
        'horse_name': 'VARCHAR(255)',
        'foreignbred_code': 'VARCHAR(255)',
        'statebred_code': 'VARCHAR(255)',
        'program_number': 'VARCHAR(255)',
        'breeder': 'VARCHAR(255)',
        'color': 'VARCHAR(255)',
        'foal_date': 'DATE',
        'age': 'INT',
        'sex': 'VARCHAR(255)',
        'sire': 'VARCHAR(255)',
        'dam': 'VARCHAR(255)',
        'broodmare_sire': 'VARCHAR(255)',
    },

    '6': {
        'track_code': 'VARCHAR(255)',
        'date': 'DATE',
        'race_num': 'INT',
        'day_evening_flag': 'VARCHAR(255)',
        'footnote_sequence': 'INT',
        'footnote_text': 'VARCHAR(255)'
    },

    'DRF': {
        'track': 'VARCHAR(255)',
        'date': 'DATE',
        'race': 'INT',
        'post_position': 'INT',
        'entry': 'VARCHAR(255)',
        'distance': 'INT',
        'surface': 'VARCHAR(255)',
        'race_type': 'VARCHAR(255)',
        'age_sex_restricts': 'VARCHAR(255)',
        'today_race_class': 'VARCHAR(255)',
        'purse': 'INT',
        'claiming_price': 'INT',
        'horse_claiming_price': 'INT',
        'track_record_pace': 'FLOAT',
        'race_conditions': 'VARCHAR(255)',
        'lasix_list': 'VARCHAR(255)',
        'bute_list': 'VARCHAR(255)',
        'coupled_list': 'VARCHAR(255)',
        'mutuel_list': 'VARCHAR(255)',
        'simulcast_track_code': 'VARCHAR(255)',
        'simulcast_track_race': 'INT',
        'breed_type': 'VARCHAR(255)',
        'today_nasal_strip_chg': 'INT',
        'allweather_surface': 'INT',

        # *** Today's Horse/Trainer/Jockey/Owner ***
        'trainer': 'VARCHAR(255)',
        'trainer_starts': 'INT',
        'trainer_wins': 'INT',
        'trainer_places': 'INT',
        'trainer_shows': 'INT',
        'jockey': 'VARCHAR(255)',
        'apprentice_wgt_alw': 'INT',
        'jockey_starts': 'INT',
        'jockey_wins': 'INT',
        'jockey_places': 'INT',
        'jockey_shows': 'INT',
        'todays_owner': 'VARCHAR(255)',
        'owners_silks': 'VARCHAR(255)',
        'main_track_only_AE': 'VARCHAR(255)',
        'program_number': 'VARCHAR(255)',
        'morning_line': 'FLOAT',

        # *** Horse History Data ***
        'horse_name': 'VARCHAR(255)',
        'birth_year': 'INT',
        'foaling_month': 'INT',
        'sex': 'VARCHAR(255)',
        'color': 'VARCHAR(255)',
        'weight': 'INT',
        'sire': 'VARCHAR(255)',
        'sires_sire': 'VARCHAR(255)',
        'dam': 'VARCHAR(255)',
        'dams_sire': 'VARCHAR(255)',
        'breeder': 'VARCHAR(255)',
        'where_bred': 'VARCHAR(255)',
        'program_post_pos': 'VARCHAR(255)',

        # *** Current Horse Stats ***
        'todays_meds_new': 'INT',
        'todays_meds_old': 'INT',
        'equipment_change': 'INT',

        #      Horse's Lifetime Record @ Today's Distance
        'life_distance_starts': 'INT',
        'life_distance_wins': 'INT',
        'life_distance_places': 'INT',
        'life_distance_shows': 'INT',
        'life_distance_earned': 'INT',

        #      Horse's Lifetime Record @ Today's track:
        'life_track_starts': 'INT',
        'life_track_wins': 'INT',
        'life_track_places': 'INT',
        'life_track_shows': 'INT',
        'life_track_earned': 'INT',

        #      Horse's Lifetime Turf Record:
        'life_turf_starts': 'INT',
        'life_turf_wins': 'INT',
        'life_turf_places': 'INT',
        'life_turf_shows': 'INT',
        'life_turf_earned': 'INT',

        #      Horse's Lifetime Wet Record:
        'life_wet_starts': 'INT',
        'life_wet_wins': 'INT',
        'life_wet_places': 'INT',
        'life_wet_shows': 'INT',
        'life_wet_earned': 'INT',
        #       Horse's Current Year Record:
        'current_year_year': 'INT',
        'current_year_starts': 'INT',
        'current_year_wins': 'INT',
        'current_year_places': 'INT',
        'current_year_shows': 'INT',
        'current_year_earned': 'INT',

        #      Horse's Previous Year Record:
        'past_year_year': 'INT',
        'past_year_starts': 'INT',
        'past_year_wins': 'INT',
        'past_year_places': 'INT',
        'past_year_shows': 'INT',
        'past_year_earned': 'INT',

        #      Horse's Lifetime Record:
        'lifetime_starts': 'INT',
        'lifetime_wins': 'INT',
        'lifetime_places': 'INT',
        'lifetime_shows': 'INT',
        'lifetime_earned': 'INT',

        #      Recent Workouts
        'workout_date_1': 'DATE',
        'workout_date_2': 'DATE',
        'workout_date_3': 'DATE',
        'workout_date_4': 'DATE',
        'workout_date_5': 'DATE',
        'workout_date_6': 'DATE',
        'workout_date_7': 'DATE',
        'workout_date_8': 'DATE',
        'workout_date_9': 'DATE',
        'workout_date_10': 'DATE',
        'workout_date_11': 'DATE',
        'workout_date_12': 'DATE',

        'workout_time_1': 'FLOAT',
        'workout_time_2': 'FLOAT',
        'workout_time_3': 'FLOAT',
        'workout_time_4': 'FLOAT',
        'workout_time_5': 'FLOAT',
        'workout_time_6': 'FLOAT',
        'workout_time_7': 'FLOAT',
        'workout_time_8': 'FLOAT',
        'workout_time_9': 'FLOAT',
        'workout_time_10': 'FLOAT',
        'workout_time_11': 'FLOAT',
        'workout_time_12': 'FLOAT',

        'workout_time_1_bullet': 'INT',
        'workout_time_2_bullet': 'INT',
        'workout_time_3_bullet': 'INT',
        'workout_time_4_bullet': 'INT',
        'workout_time_5_bullet': 'INT',
        'workout_time_6_bullet': 'INT',
        'workout_time_7_bullet': 'INT',
        'workout_time_8_bullet': 'INT',
        'workout_time_9_bullet': 'INT',
        'workout_time_10_bullet': 'INT',

        'workout_track_1': 'VARCHAR(255)',
        'workout_track_2': 'VARCHAR(255)',
        'workout_track_3': 'VARCHAR(255)',
        'workout_track_4': 'VARCHAR(255)',
        'workout_track_5': 'VARCHAR(255)',
        'workout_track_6': 'VARCHAR(255)',
        'workout_track_7': 'VARCHAR(255)',
        'workout_track_8': 'VARCHAR(255)',
        'workout_track_9': 'VARCHAR(255)',
        'workout_track_10': 'VARCHAR(255)',
        'workout_track_11': 'VARCHAR(255)',
        'workout_track_12': 'VARCHAR(255)',

        'workout_distance_1': 'INT',
        'workout_distance_2': 'INT',
        'workout_distance_3': 'INT',
        'workout_distance_4': 'INT',
        'workout_distance_5': 'INT',
        'workout_distance_6': 'INT',
        'workout_distance_7': 'INT',
        'workout_distance_8': 'INT',
        'workout_distance_9': 'INT',
        'workout_distance_10': 'INT',
        'workout_distance_11': 'INT',
        'workout_distance_12': 'INT',

        'workout_condition_1': 'VARCHAR(255)',
        'workout_condition_2': 'VARCHAR(255)',
        'workout_condition_3': 'VARCHAR(255)',
        'workout_condition_4': 'VARCHAR(255)',
        'workout_condition_5': 'VARCHAR(255)',
        'workout_condition_6': 'VARCHAR(255)',
        'workout_condition_7': 'VARCHAR(255)',
        'workout_condition_8': 'VARCHAR(255)',
        'workout_condition_9': 'VARCHAR(255)',
        'workout_condition_10': 'VARCHAR(255)',
        'workout_condition_11': 'VARCHAR(255)',
        'workout_condition_12': 'VARCHAR(255)',

        'workout_description_1': 'VARCHAR(255)',
        'workout_description_2': 'VARCHAR(255)',
        'workout_description_3': 'VARCHAR(255)',
        'workout_description_4': 'VARCHAR(255)',
        'workout_description_5': 'VARCHAR(255)',
        'workout_description_6': 'VARCHAR(255)',
        'workout_description_7': 'VARCHAR(255)',
        'workout_description_8': 'VARCHAR(255)',
        'workout_description_9': 'VARCHAR(255)',
        'workout_description_10': 'VARCHAR(255)',
        'workout_description_11': 'VARCHAR(255)',
        'workout_description_12': 'VARCHAR(255)',

        'workout_track_type_1': 'VARCHAR(255)',
        'workout_track_type_2': 'VARCHAR(255)',
        'workout_track_type_3': 'VARCHAR(255)',
        'workout_track_type_4': 'VARCHAR(255)',
        'workout_track_type_5': 'VARCHAR(255)',
        'workout_track_type_6': 'VARCHAR(255)',
        'workout_track_type_7': 'VARCHAR(255)',
        'workout_track_type_8': 'VARCHAR(255)',
        'workout_track_type_9': 'VARCHAR(255)',
        'workout_track_type_10': 'VARCHAR(255)',
        'workout_track_type_11': 'VARCHAR(255)',
        'workout_track_type_12': 'VARCHAR(255)',

        'same_workouts_all_day_1': 'INT',
        'same_workouts_all_day_2': 'INT',
        'same_workouts_all_day_3': 'INT',
        'same_workouts_all_day_4': 'INT',
        'same_workouts_all_day_5': 'INT',
        'same_workouts_all_day_6': 'INT',
        'same_workouts_all_day_7': 'INT',
        'same_workouts_all_day_8': 'INT',
        'same_workouts_all_day_9': 'INT',
        'same_workouts_all_day_10': 'INT',
        'same_workouts_all_day_11': 'INT',
        'same_workouts_all_day_12': 'INT',

        'rank_same_workout_1': 'INT',
        'rank_same_workout_2': 'INT',
        'rank_same_workout_3': 'INT',
        'rank_same_workout_4': 'INT',
        'rank_same_workout_5': 'INT',
        'rank_same_workout_6': 'INT',
        'rank_same_workout_7': 'INT',
        'rank_same_workout_8': 'INT',
        'rank_same_workout_9': 'INT',
        'rank_same_workout_10': 'INT',
        'rank_same_workout_11': 'INT',
        'rank_same_workout_12': 'INT',


        'bris_run_style': 'VARCHAR(255)',
        'quirin_speed_points': 'INT',
        '2f_bris_pace_par': 'INT',
        '4f_bris_pace_par': 'INT',
        '6f_bris_pace_par': 'INT',
        'bris_speed_par': 'INT',
        'bris_late_pace_par': 'INT',

        'TJ_starts': 'INT',
        'TJ_wins': 'INT',
        'TJ_places': 'INT',
        'TJ_shows': 'INT',
        'TJ_roi': 'INT',

        'days_since_last_race': 'INT',

        'race_conditions_1': 'VARCHAR(255)',
        'race_conditions_2': 'VARCHAR(255)',
        'race_conditions_3': 'VARCHAR(255)',
        'race_conditions_4': 'VARCHAR(255)',
        'race_conditions_5': 'VARCHAR(255)',
        'race_conditions_6': 'VARCHAR(255)',

        'life_starts_alw': 'INT',
        'life_wins_alw': 'INT',
        'life_places_alw': 'INT',
        'life_shows_alw': 'INT',
        'life_earnings_alw': 'INT',
        'best_bris_speed_alw': 'INT',
        'low_claiming_price': 'INT',
        'statebread_flag': 'INT',

        'wager_type_1': 'VARCHAR(255)',
        'wager_type_2': 'VARCHAR(255)',
        'wager_type_3': 'VARCHAR(255)',
        'wager_type_4': 'VARCHAR(255)',
        'wager_type_5': 'VARCHAR(255)',
        'wager_type_6': 'VARCHAR(255)',
        'wager_type_7': 'VARCHAR(255)',
        'wager_type_8': 'VARCHAR(255)',
        'wager_type_9': 'VARCHAR(255)',

        'bris_prime_power': 'INT',

        #      *** Horse's Past Performace Data for last 10 races ***
        #      For each of the last 10 races (most recent to furthest back):
        'past_race_date_1': 'DATE',
        'past_race_date_2': 'DATE',
        'past_race_date_3': 'DATE',
        'past_race_date_4': 'DATE',
        'past_race_date_5': 'DATE',
        'past_race_date_6': 'DATE',
        'past_race_date_7': 'DATE',
        'past_race_date_8': 'DATE',
        'past_race_date_9': 'DATE',
        'past_race_date_10': 'DATE',

        'past_days_since_last_1': 'INT',
        'past_days_since_last_2': 'INT',
        'past_days_since_last_3': 'INT',
        'past_days_since_last_4': 'INT',
        'past_days_since_last_5': 'INT',
        'past_days_since_last_6': 'INT',
        'past_days_since_last_7': 'INT',
        'past_days_since_last_8': 'INT',
        'past_days_since_last_9': 'INT',
        'maybe_reservd275': 'INT',

        'past_track_code_1': 'VARCHAR(255)',
        'past_track_code_2': 'VARCHAR(255)',
        'past_track_code_3': 'VARCHAR(255)',
        'past_track_code_4': 'VARCHAR(255)',
        'past_track_code_5': 'VARCHAR(255)',
        'past_track_code_6': 'VARCHAR(255)',
        'past_track_code_7': 'VARCHAR(255)',
        'past_track_code_8': 'VARCHAR(255)',
        'past_track_code_9': 'VARCHAR(255)',
        'past_track_code_10': 'VARCHAR(255)',

        'past_BRIS_track_code_1': 'VARCHAR(255)',
        'past_BRIS_track_code_2': 'VARCHAR(255)',
        'past_BRIS_track_code_3': 'VARCHAR(255)',
        'past_BRIS_track_code_4': 'VARCHAR(255)',
        'past_BRIS_track_code_5': 'VARCHAR(255)',
        'past_BRIS_track_code_6': 'VARCHAR(255)',
        'past_BRIS_track_code_7': 'VARCHAR(255)',
        'past_BRIS_track_code_8': 'VARCHAR(255)',
        'past_BRIS_track_code_9': 'VARCHAR(255)',
        'past_BRIS_track_code_10': 'VARCHAR(255)',

        'past_race_number_1': 'INT',
        'past_race_number_2': 'INT',
        'past_race_number_3': 'INT',
        'past_race_number_4': 'INT',
        'past_race_number_5': 'INT',
        'past_race_number_6': 'INT',
        'past_race_number_7': 'INT',
        'past_race_number_8': 'INT',
        'past_race_number_9': 'INT',
        'past_race_number_10': 'INT',

        'past_track_cond_1': 'VARCHAR(255)',
        'past_track_cond_2': 'VARCHAR(255)',
        'past_track_cond_3': 'VARCHAR(255)',
        'past_track_cond_4': 'VARCHAR(255)',
        'past_track_cond_5': 'VARCHAR(255)',
        'past_track_cond_6': 'VARCHAR(255)',
        'past_track_cond_7': 'VARCHAR(255)',
        'past_track_cond_8': 'VARCHAR(255)',
        'past_track_cond_9': 'VARCHAR(255)',
        'past_track_cond_10': 'VARCHAR(255)',

        'past_distance_1': 'INT',
        'past_distance_2': 'INT',
        'past_distance_3': 'INT',
        'past_distance_4': 'INT',
        'past_distance_5': 'INT',
        'past_distance_6': 'INT',
        'past_distance_7': 'INT',
        'past_distance_8': 'INT',
        'past_distance_9': 'INT',
        'past_distance_10': 'INT',

        'past_distance_1_about_flag': 'INT',
        'past_distance_2_about_flag': 'INT',
        'past_distance_3_about_flag': 'INT',
        'past_distance_4_about_flag': 'INT',
        'past_distance_5_about_flag': 'INT',
        'past_distance_6_about_flag': 'INT',
        'past_distance_7_about_flag': 'INT',
        'past_distance_8_about_flag': 'INT',
        'past_distance_9_about_flag': 'INT',
        'past_distance_10_about_flag': 'INT',

        'past_surface_1': 'VARCHAR(255)',
        'past_surface_2': 'VARCHAR(255)',
        'past_surface_3': 'VARCHAR(255)',
        'past_surface_4': 'VARCHAR(255)',
        'past_surface_5': 'VARCHAR(255)',
        'past_surface_6': 'VARCHAR(255)',
        'past_surface_7': 'VARCHAR(255)',
        'past_surface_8': 'VARCHAR(255)',
        'past_surface_9': 'VARCHAR(255)',
        'past_surface_10': 'VARCHAR(255)',

        ##      Special Chute Indicator
        'past_special_chute_1': 'INT',
        'past_special_chute_2': 'INT',
        'past_special_chute_3': 'INT',
        'past_special_chute_4': 'INT',
        'past_special_chute_5': 'INT',
        'past_special_chute_6': 'INT',
        'past_special_chute_7': 'INT',
        'past_special_chute_8': 'INT',
        'past_special_chute_9': 'INT',
        'past_special_chute_10': 'INT',

        ## Number of entrants
        'past_entrants_1': 'INT',
        'past_entrants_2': 'INT',
        'past_entrants_3': 'INT',
        'past_entrants_4': 'INT',
        'past_entrants_5': 'INT',
        'past_entrants_6': 'INT',
        'past_entrants_7': 'INT',
        'past_entrants_8': 'INT',
        'past_entrants_9': 'INT',
        'past_entrants_10': 'INT',

        ##      Past post position

        'past_post_1': 'INT',
        'past_post_2': 'INT',
        'past_post_3': 'INT',
        'past_post_4': 'INT',
        'past_post_5': 'INT',
        'past_post_6': 'INT',
        'past_post_7': 'INT',
        'past_post_8': 'INT',
        'past_post_9': 'INT',
        'past_post_10': 'INT',

        # Equipment                                                                    b - blinkers
        'past_equipment_1': 'INT',
        'past_equipment_2': 'INT',
        'past_equipment_3': 'INT',
        'past_equipment_4': 'INT',
        'past_equipment_5': 'INT',
        'past_equipment_6': 'INT',
        'past_equipment_7': 'INT',
        'past_equipment_8': 'INT',
        'past_equipment_9': 'INT',
        'past_equipment_10': 'INT',

        ##      Race name of previous races
        'past_race_name_1': 'VARCHAR(255)',
        'past_race_name_2': 'VARCHAR(255)',
        'past_race_name_3': 'VARCHAR(255)',
        'past_race_name_4': 'VARCHAR(255)',
        'past_race_name_5': 'VARCHAR(255)',
        'past_race_name_6': 'VARCHAR(255)',
        'past_race_name_7': 'VARCHAR(255)',
        'past_race_name_8': 'VARCHAR(255)',
        'past_race_name_9': 'VARCHAR(255)',
        'past_race_name_10': 'VARCHAR(255)',

        ##      Medication
        'past_medication_1': 'INT',
        'past_medication_2': 'INT',
        'past_medication_3': 'INT',
        'past_medication_4': 'INT',
        'past_medication_5': 'INT',
        'past_medication_6': 'INT',
        'past_medication_7': 'INT',
        'past_medication_8': 'INT',
        'past_medication_9': 'INT',
        'past_medication_10': 'INT',

        'past_medication_1_lasix': 'INT',
        'past_medication_2_lasix': 'INT',
        'past_medication_3_lasix': 'INT',
        'past_medication_4_lasix': 'INT',
        'past_medication_5_lasix': 'INT',
        'past_medication_6_lasix': 'INT',
        'past_medication_7_lasix': 'INT',
        'past_medication_8_lasix': 'INT',
        'past_medication_9_lasix': 'INT',
        'past_medication_10_lasix': 'INT',

        'past_medication_1_bute': 'INT',
        'past_medication_2_bute': 'INT',
        'past_medication_3_bute': 'INT',
        'past_medication_4_bute': 'INT',
        'past_medication_5_bute': 'INT',
        'past_medication_6_bute': 'INT',
        'past_medication_7_bute': 'INT',
        'past_medication_8_bute': 'INT',
        'past_medication_9_bute': 'INT',
        'past_medication_10_bute': 'INT',

        ##      Trip Comment
        'past_trip_comment_1': 'VARCHAR(255)',
        'past_trip_comment_2': 'VARCHAR(255)',
        'past_trip_comment_3': 'VARCHAR(255)',
        'past_trip_comment_4': 'VARCHAR(255)',
        'past_trip_comment_5': 'VARCHAR(255)',
        'past_trip_comment_6': 'VARCHAR(255)',
        'past_trip_comment_7': 'VARCHAR(255)',
        'past_trip_comment_8': 'VARCHAR(255)',
        'past_trip_comment_9': 'VARCHAR(255)',
        'past_trip_comment_10': 'VARCHAR(255)',

        ##      Winner, Place, and Show horse names
        'past_win_1': 'VARCHAR(255)',
        'past_win_2': 'VARCHAR(255)',
        'past_win_3': 'VARCHAR(255)',
        'past_win_4': 'VARCHAR(255)',
        'past_win_5': 'VARCHAR(255)',
        'past_win_6': 'VARCHAR(255)',
        'past_win_7': 'VARCHAR(255)',
        'past_win_8': 'VARCHAR(255)',
        'past_win_9': 'VARCHAR(255)',
        'past_win_10': 'VARCHAR(255)',

        'past_place_1': 'VARCHAR(255)',
        'past_place_2': 'VARCHAR(255)',
        'past_place_3': 'VARCHAR(255)',
        'past_place_4': 'VARCHAR(255)',
        'past_place_5': 'VARCHAR(255)',
        'past_place_6': 'VARCHAR(255)',
        'past_place_7': 'VARCHAR(255)',
        'past_place_8': 'VARCHAR(255)',
        'past_place_9': 'VARCHAR(255)',
        'past_place_10': 'VARCHAR(255)',

        'past_show_1': 'VARCHAR(255)',
        'past_show_2': 'VARCHAR(255)',
        'past_show_3': 'VARCHAR(255)',
        'past_show_4': 'VARCHAR(255)',
        'past_show_5': 'VARCHAR(255)',
        'past_show_6': 'VARCHAR(255)',
        'past_show_7': 'VARCHAR(255)',
        'past_show_8': 'VARCHAR(255)',
        'past_show_9': 'VARCHAR(255)',
        'past_show_10': 'VARCHAR(255)',

        ##      Winner, Place, and Show Weight Carried
        'past_win_weight_1': 'INT',
        'past_win_weight_2': 'INT',
        'past_win_weight_3': 'INT',
        'past_win_weight_4': 'INT',
        'past_win_weight_5': 'INT',
        'past_win_weight_6': 'INT',
        'past_win_weight_7': 'INT',
        'past_win_weight_8': 'INT',
        'past_win_weight_9': 'INT',
        'past_win_weight_10': 'INT',

        'past_place_weight_1': 'INT',
        'past_place_weight_2': 'INT',
        'past_place_weight_3': 'INT',
        'past_place_weight_4': 'INT',
        'past_place_weight_5': 'INT',
        'past_place_weight_6': 'INT',
        'past_place_weight_7': 'INT',
        'past_place_weight_8': 'INT',
        'past_place_weight_9': 'INT',
        'past_place_weight_10': 'INT',

        'past_show_weight_1': 'INT',
        'past_show_weight_2': 'INT',
        'past_show_weight_3': 'INT',
        'past_show_weight_4': 'INT',
        'past_show_weight_5': 'INT',
        'past_show_weight_6': 'INT',
        'past_show_weight_7': 'INT',
        'past_show_weight_8': 'INT',
        'past_show_weight_9': 'INT',
        'past_show_weight_10': 'INT',

        ##      Past Winner, Place, and Show Margins
        'past_win_margin_1': 'FLOAT',
        'past_win_margin_2': 'FLOAT',
        'past_win_margin_3': 'FLOAT',
        'past_win_margin_4': 'FLOAT',
        'past_win_margin_5': 'FLOAT',
        'past_win_margin_6': 'FLOAT',
        'past_win_margin_7': 'FLOAT',
        'past_win_margin_8': 'FLOAT',
        'past_win_margin_9': 'FLOAT',
        'past_win_margin_10': 'FLOAT',

        'past_place_margin_1': 'FLOAT',
        'past_place_margin_2': 'FLOAT',
        'past_place_margin_3': 'FLOAT',
        'past_place_margin_4': 'FLOAT',
        'past_place_margin_5': 'FLOAT',
        'past_place_margin_6': 'FLOAT',
        'past_place_margin_7': 'FLOAT',
        'past_place_margin_8': 'FLOAT',
        'past_place_margin_9': 'FLOAT',
        'past_place_margin_10': 'FLOAT',

        'past_show_margin_1': 'FLOAT',
        'past_show_margin_2': 'FLOAT',
        'past_show_margin_3': 'FLOAT',
        'past_show_margin_4': 'FLOAT',
        'past_show_margin_5': 'FLOAT',
        'past_show_margin_6': 'FLOAT',
        'past_show_margin_7': 'FLOAT',
        'past_show_margin_8': 'FLOAT',
        'past_show_margin_9': 'FLOAT',
        'past_show_margin_10': 'FLOAT',

        ##      Alternate/Extra Comment Line
        'past_extra_comment_1': 'VARCHAR(255)',
        'past_extra_comment_2': 'VARCHAR(255)',
        'past_extra_comment_3': 'VARCHAR(255)',
        'past_extra_comment_4': 'VARCHAR(255)',
        'past_extra_comment_5': 'VARCHAR(255)',
        'past_extra_comment_6': 'VARCHAR(255)',
        'past_extra_comment_7': 'VARCHAR(255)',
        'past_extra_comment_8': 'VARCHAR(255)',
        'past_extra_comment_9': 'VARCHAR(255)',
        'past_extra_comment_10': 'VARCHAR(255)',

        'past_weight_1': 'INT',
        'past_weight_2': 'INT',
        'past_weight_3': 'INT',
        'past_weight_4': 'INT',
        'past_weight_5': 'INT',
        'past_weight_6': 'INT',
        'past_weight_7': 'INT',
        'past_weight_8': 'INT',
        'past_weight_9': 'INT',
        'past_weight_10': 'INT',

        'past_odds_1': 'FLOAT',
        'past_odds_2': 'FLOAT',
        'past_odds_3': 'FLOAT',
        'past_odds_4': 'FLOAT',
        'past_odds_5': 'FLOAT',
        'past_odds_6': 'FLOAT',
        'past_odds_7': 'FLOAT',
        'past_odds_8': 'FLOAT',
        'past_odds_9': 'FLOAT',
        'past_odds_10': 'FLOAT',

        'past_entry_1': 'INT',
        'past_entry_2': 'INT',
        'past_entry_3': 'INT',
        'past_entry_4': 'INT',
        'past_entry_5': 'INT',
        'past_entry_6': 'INT',
        'past_entry_7': 'INT',
        'past_entry_8': 'INT',
        'past_entry_9': 'INT',
        'past_entry_10': 'INT',

        'past_race_class_1': 'VARCHAR(255)',
        'past_race_class_2': 'VARCHAR(255)',        ##      537     CHARACTER               25
        'past_race_class_3': 'VARCHAR(255)',        ##      538     CHARACTER               25
        'past_race_class_4': 'VARCHAR(255)',        ##      539     CHARACTER               25
        'past_race_class_5': 'VARCHAR(255)',        ##      540     CHARACTER               25
        'past_race_class_6': 'VARCHAR(255)',        ##      541     CHARACTER               25
        'past_race_class_7': 'VARCHAR(255)',        ##      542     CHARACTER               25
        'past_race_class_8': 'VARCHAR(255)',        ##      543     CHARACTER               25
        'past_race_class_9': 'VARCHAR(255)',        ##      544     CHARACTER               25
        'past_race_class_10': 'VARCHAR(255)',       ##      545     CHARACTER               25

        ##      Claiming Price (of horse)
        'past_claim_price_1': 'INT',
        'past_claim_price_2': 'INT',
        'past_claim_price_3': 'INT',
        'past_claim_price_4': 'INT',
        'past_claim_price_5': 'INT',
        'past_claim_price_6': 'INT',
        'past_claim_price_7': 'INT',
        'past_claim_price_8': 'INT',
        'past_claim_price_9': 'INT',
        'past_claim_price_10': 'INT',

        'past_purse_1': 'INT',
        'past_purse_2': 'INT',
        'past_purse_3': 'INT',
        'past_purse_4': 'INT',
        'past_purse_5': 'INT',
        'past_purse_6': 'INT',
        'past_purse_7': 'INT',
        'past_purse_8': 'INT',
        'past_purse_9': 'INT',
        'past_purse_10': 'INT',

        ##      Start call position
        'past_call_pos_start_1': 'INT',
        'past_call_pos_start_2': 'INT',
        'past_call_pos_start_3': 'INT',
        'past_call_pos_start_4': 'INT',
        'past_call_pos_start_5': 'INT',
        'past_call_pos_start_6': 'INT',
        'past_call_pos_start_7': 'INT',
        'past_call_pos_start_8': 'INT',
        'past_call_pos_start_9': 'INT',
        'past_call_pos_start_10': 'INT',

        'past_call_pos_first_1': 'INT',
        'past_call_pos_first_2': 'INT',
        'past_call_pos_first_3': 'INT',
        'past_call_pos_first_4': 'INT',
        'past_call_pos_first_5': 'INT',
        'past_call_pos_first_6': 'INT',
        'past_call_pos_first_7': 'INT',
        'past_call_pos_first_8': 'INT',
        'past_call_pos_first_9': 'INT',
        'past_call_pos_first_10': 'INT',

        'past_call_pos_second_1': 'INT',
        'past_call_pos_second_2': 'INT',
        'past_call_pos_second_3': 'INT',
        'past_call_pos_second_4': 'INT',
        'past_call_pos_second_5': 'INT',
        'past_call_pos_second_6': 'INT',
        'past_call_pos_second_7': 'INT',
        'past_call_pos_second_8': 'INT',
        'past_call_pos_second_9': 'INT',
        'past_call_pos_second_10': 'INT',

        'past_call_pos_gate_1': 'INT',
        'past_call_pos_gate_2': 'INT',
        'past_call_pos_gate_3': 'INT',
        'past_call_pos_gate_4': 'INT',
        'past_call_pos_gate_5': 'INT',
        'past_call_pos_gate_6': 'INT',
        'past_call_pos_gate_7': 'INT',
        'past_call_pos_gate_8': 'INT',
        'past_call_pos_gate_9': 'INT',
        'past_call_pos_gate_10': 'INT',

        'past_call_pos_stretch_1': 'INT',
        'past_call_pos_stretch_2': 'INT',
        'past_call_pos_stretch_3': 'INT',
        'past_call_pos_stretch_4': 'INT',
        'past_call_pos_stretch_5': 'INT',
        'past_call_pos_stretch_6': 'INT',
        'past_call_pos_stretch_7': 'INT',
        'past_call_pos_stretch_8': 'INT',
        'past_call_pos_stretch_9': 'INT',
        'past_call_pos_stretch_10': 'INT',

        'past_call_pos_finish_1': 'INT',
        'past_call_pos_finish_2': 'INT',
        'past_call_pos_finish_3': 'INT',
        'past_call_pos_finish_4': 'INT',
        'past_call_pos_finish_5': 'INT',
        'past_call_pos_finish_6': 'INT',
        'past_call_pos_finish_7': 'INT',
        'past_call_pos_finish_8': 'INT',
        'past_call_pos_finish_9': 'INT',
        'past_call_pos_finish_10': 'INT',

        'past_money_pos_1': 'INT',
        'past_money_pos_2': 'INT',
        'past_money_pos_3': 'INT',
        'past_money_pos_4': 'INT',
        'past_money_pos_5': 'INT',
        'past_money_pos_6': 'INT',
        'past_money_pos_7': 'INT',
        'past_money_pos_8': 'INT',
        'past_money_pos_9': 'INT',
        'past_money_pos_10': 'INT',

        # Combined lead/beaten lengths columns. Negative values for trailing horses,
        # and positive values for the leader.

        'past_lead_or_beaten_lengths_start_1': 'FLOAT',
        'past_lead_or_beaten_lengths_start_2': 'FLOAT',
        'past_lead_or_beaten_lengths_start_3': 'FLOAT',
        'past_lead_or_beaten_lengths_start_4': 'FLOAT',
        'past_lead_or_beaten_lengths_start_5': 'FLOAT',
        'past_lead_or_beaten_lengths_start_6': 'FLOAT',
        'past_lead_or_beaten_lengths_start_7': 'FLOAT',
        'past_lead_or_beaten_lengths_start_8': 'FLOAT',
        'past_lead_or_beaten_lengths_start_9': 'FLOAT',
        'past_lead_or_beaten_lengths_start_10': 'FLOAT',

        'past_lead_or_beaten_lengths_first_call_1': 'FLOAT',
        'past_lead_or_beaten_lengths_first_call_2': 'FLOAT',
        'past_lead_or_beaten_lengths_first_call_3': 'FLOAT',
        'past_lead_or_beaten_lengths_first_call_4': 'FLOAT',
        'past_lead_or_beaten_lengths_first_call_5': 'FLOAT',
        'past_lead_or_beaten_lengths_first_call_6': 'FLOAT',
        'past_lead_or_beaten_lengths_first_call_7': 'FLOAT',
        'past_lead_or_beaten_lengths_first_call_8': 'FLOAT',
        'past_lead_or_beaten_lengths_first_call_9': 'FLOAT',
        'past_lead_or_beaten_lengths_first_call_10': 'FLOAT',

        'past_lead_or_beaten_lengths_second_call_1': 'FLOAT',
        'past_lead_or_beaten_lengths_second_call_2': 'FLOAT',
        'past_lead_or_beaten_lengths_second_call_3': 'FLOAT',
        'past_lead_or_beaten_lengths_second_call_4': 'FLOAT',
        'past_lead_or_beaten_lengths_second_call_5': 'FLOAT',
        'past_lead_or_beaten_lengths_second_call_6': 'FLOAT',
        'past_lead_or_beaten_lengths_second_call_7': 'FLOAT',
        'past_lead_or_beaten_lengths_second_call_8': 'FLOAT',
        'past_lead_or_beaten_lengths_second_call_9': 'FLOAT',
        'past_lead_or_beaten_lengths_second_call_10': 'FLOAT',

        'past_lead_or_beaten_lengths_stretch_call_1': 'FLOAT',
        'past_lead_or_beaten_lengths_stretch_call_2': 'FLOAT',
        'past_lead_or_beaten_lengths_stretch_call_3': 'FLOAT',
        'past_lead_or_beaten_lengths_stretch_call_4': 'FLOAT',
        'past_lead_or_beaten_lengths_stretch_call_5': 'FLOAT',
        'past_lead_or_beaten_lengths_stretch_call_6': 'FLOAT',
        'past_lead_or_beaten_lengths_stretch_call_7': 'FLOAT',
        'past_lead_or_beaten_lengths_stretch_call_8': 'FLOAT',
        'past_lead_or_beaten_lengths_stretch_call_9': 'FLOAT',
        'past_lead_or_beaten_lengths_stretch_call_10': 'FLOAT',

        'past_lead_or_beaten_lengths_finish_1': 'FLOAT',
        'past_lead_or_beaten_lengths_finish_2': 'FLOAT',
        'past_lead_or_beaten_lengths_finish_3': 'FLOAT',
        'past_lead_or_beaten_lengths_finish_4': 'FLOAT',
        'past_lead_or_beaten_lengths_finish_5': 'FLOAT',
        'past_lead_or_beaten_lengths_finish_6': 'FLOAT',
        'past_lead_or_beaten_lengths_finish_7': 'FLOAT',
        'past_lead_or_beaten_lengths_finish_8': 'FLOAT',
        'past_lead_or_beaten_lengths_finish_9': 'FLOAT',
        'past_lead_or_beaten_lengths_finish_10': 'FLOAT',


        ##      Start Call - Beaten lengths/Leader margin
        'past_lead_margin_start_1': 'FLOAT',
        'past_lead_margin_start_2': 'FLOAT',
        'past_lead_margin_start_3': 'FLOAT',
        'past_lead_margin_start_4': 'FLOAT',
        'past_lead_margin_start_5': 'FLOAT',
        'past_lead_margin_start_6': 'FLOAT',
        'past_lead_margin_start_7': 'FLOAT',
        'past_lead_margin_start_8': 'FLOAT',
        'past_lead_margin_start_9': 'FLOAT',
        'past_lead_margin_start_10': 'FLOAT',

        ##      Start Call - Beaten lengths only
        'past_beaten_lengths_start_1': 'FLOAT',
        'past_beaten_lengths_start_2': 'FLOAT',
        'past_beaten_lengths_start_3': 'FLOAT',
        'past_beaten_lengths_start_4': 'FLOAT',
        'past_beaten_lengths_start_5': 'FLOAT',
        'past_beaten_lengths_start_6': 'FLOAT',
        'past_beaten_lengths_start_7': 'FLOAT',
        'past_beaten_lengths_start_8': 'FLOAT',
        'past_beaten_lengths_start_9': 'FLOAT',
        'past_beaten_lengths_start_10': 'FLOAT',

        ##      1st Call Beaten lengths/Leader margin
        'past_lead_margin_first_call_1': 'FLOAT',
        'past_lead_margin_first_call_2': 'FLOAT',
        'past_lead_margin_first_call_3': 'FLOAT',
        'past_lead_margin_first_call_4': 'FLOAT',
        'past_lead_margin_first_call_5': 'FLOAT',
        'past_lead_margin_first_call_6': 'FLOAT',
        'past_lead_margin_first_call_7': 'FLOAT',
        'past_lead_margin_first_call_8': 'FLOAT',
        'past_lead_margin_first_call_9': 'FLOAT',
        'past_lead_margin_first_call_10': 'FLOAT',

        ##      1st Call Beathen lengths only
        'past_beaten_lengths_first_call_1': 'FLOAT',
        'past_beaten_lengths_first_call_2': 'FLOAT',
        'past_beaten_lengths_first_call_3': 'FLOAT',
        'past_beaten_lengths_first_call_4': 'FLOAT',
        'past_beaten_lengths_first_call_5': 'FLOAT',
        'past_beaten_lengths_first_call_6': 'FLOAT',
        'past_beaten_lengths_first_call_7': 'FLOAT',
        'past_beaten_lengths_first_call_8': 'FLOAT',
        'past_beaten_lengths_first_call_9': 'FLOAT',
        'past_beaten_lengths_first_call_10': 'FLOAT',

        ##      2d Call Beaten Lengths/Leader margin
        'past_lead_margin_second_call_1': 'FLOAT',
        'past_lead_margin_second_call_2': 'FLOAT',
        'past_lead_margin_second_call_3': 'FLOAT',
        'past_lead_margin_second_call_4': 'FLOAT',
        'past_lead_margin_second_call_5': 'FLOAT',
        'past_lead_margin_second_call_6': 'FLOAT',
        'past_lead_margin_second_call_7': 'FLOAT',
        'past_lead_margin_second_call_8': 'FLOAT',
        'past_lead_margin_second_call_9': 'FLOAT',
        'past_lead_margin_second_call_10': 'FLOAT',

        ##      2d Call Beath lengths only
        'past_beaten_lengths_second_call_1': 'FLOAT',
        'past_beaten_lengths_second_call_2': 'FLOAT',
        'past_beaten_lengths_second_call_3': 'FLOAT',
        'past_beaten_lengths_second_call_4': 'FLOAT',
        'past_beaten_lengths_second_call_5': 'FLOAT',
        'past_beaten_lengths_second_call_6': 'FLOAT',
        'past_beaten_lengths_second_call_7': 'FLOAT',
        'past_beaten_lengths_second_call_8': 'FLOAT',
        'past_beaten_lengths_second_call_9': 'FLOAT',
        'past_beaten_lengths_second_call_10': 'FLOAT',

        ##      BRIS Race Shape- 1st Call
        'past_bris_shape_first_call_1': 'INT',
        'past_bris_shape_first_call_2': 'INT',
        'past_bris_shape_first_call_3': 'INT',
        'past_bris_shape_first_call_4': 'INT',
        'past_bris_shape_first_call_5': 'INT',
        'past_bris_shape_first_call_6': 'INT',
        'past_bris_shape_first_call_7': 'INT',
        'past_bris_shape_first_call_8': 'INT',
        'past_bris_shape_first_call_9': 'INT',
        'past_bris_shape_first_call_10': 'INT',

        ##      Stretch beaten lengths/leader margin
        'past_lead_margin_stretch_call_1': 'FLOAT',
        'past_lead_margin_stretch_call_2': 'FLOAT',
        'past_lead_margin_stretch_call_3': 'FLOAT',
        'past_lead_margin_stretch_call_4': 'FLOAT',
        'past_lead_margin_stretch_call_5': 'FLOAT',
        'past_lead_margin_stretch_call_6': 'FLOAT',
        'past_lead_margin_stretch_call_7': 'FLOAT',
        'past_lead_margin_stretch_call_8': 'FLOAT',
        'past_lead_margin_stretch_call_9': 'FLOAT',
        'past_lead_margin_stretch_call_10': 'FLOAT',

        ##      Stretch beaten lengths only
        'past_beaten_lengths_stretch_call_1': 'FLOAT',
        'past_beaten_lengths_stretch_call_2': 'FLOAT',
        'past_beaten_lengths_stretch_call_3': 'FLOAT',
        'past_beaten_lengths_stretch_call_4': 'FLOAT',
        'past_beaten_lengths_stretch_call_5': 'FLOAT',
        'past_beaten_lengths_stretch_call_6': 'FLOAT',
        'past_beaten_lengths_stretch_call_7': 'FLOAT',
        'past_beaten_lengths_stretch_call_8': 'FLOAT',
        'past_beaten_lengths_stretch_call_9': 'FLOAT',
        'past_beaten_lengths_stretch_call_10': 'FLOAT',

        ## Finish Beaten lengths/leader margin
        'past_lead_margin_finish_1': 'FLOAT',
        'past_lead_margin_finish_2': 'FLOAT',
        'past_lead_margin_finish_3': 'FLOAT',
        'past_lead_margin_finish_4': 'FLOAT',
        'past_lead_margin_finish_5': 'FLOAT',
        'past_lead_margin_finish_6': 'FLOAT',
        'past_lead_margin_finish_7': 'FLOAT',
        'past_lead_margin_finish_8': 'FLOAT',
        'past_lead_margin_finish_9': 'FLOAT',
        'past_lead_margin_finish_10': 'FLOAT',

        ##      Finish beaten lengths only
        'past_beaten_lengths_finish_1': 'FLOAT',
        'past_beaten_lengths_finish_2': 'FLOAT',
        'past_beaten_lengths_finish_3': 'FLOAT',
        'past_beaten_lengths_finish_4': 'FLOAT',
        'past_beaten_lengths_finish_5': 'FLOAT',
        'past_beaten_lengths_finish_6': 'FLOAT',
        'past_beaten_lengths_finish_7': 'FLOAT',
        'past_beaten_lengths_finish_8': 'FLOAT',
        'past_beaten_lengths_finish_9': 'FLOAT',
        'past_beaten_lengths_finish_10': 'FLOAT',

        ##      BRIS Race Shape 2d Call
        'past_bris_shape_second_call_1': 'INT',
        'past_bris_shape_second_call_2': 'INT',
        'past_bris_shape_second_call_3': 'INT',
        'past_bris_shape_second_call_4': 'INT',
        'past_bris_shape_second_call_5': 'INT',
        'past_bris_shape_second_call_6': 'INT',
        'past_bris_shape_second_call_7': 'INT',
        'past_bris_shape_second_call_8': 'INT',
        'past_bris_shape_second_call_9': 'INT',
        'past_bris_shape_second_call_10': 'INT',

        ##      BRIS Pace Figures
        'past_bris_pace_2f_1': 'INT',
        'past_bris_pace_2f_2': 'INT',
        'past_bris_pace_2f_3': 'INT',
        'past_bris_pace_2f_4': 'INT',
        'past_bris_pace_2f_5': 'INT',
        'past_bris_pace_2f_6': 'INT',
        'past_bris_pace_2f_7': 'INT',
        'past_bris_pace_2f_8': 'INT',
        'past_bris_pace_2f_9': 'INT',
        'past_bris_pace_2f_10': 'INT',

        'past_bris_pace_4f_1': 'INT',
        'past_bris_pace_4f_2': 'INT',
        'past_bris_pace_4f_3': 'INT',
        'past_bris_pace_4f_4': 'INT',
        'past_bris_pace_4f_5': 'INT',
        'past_bris_pace_4f_6': 'INT',
        'past_bris_pace_4f_7': 'INT',
        'past_bris_pace_4f_8': 'INT',
        'past_bris_pace_4f_9': 'INT',
        'past_bris_pace_4f_10': 'INT',

        'past_bris_pace_6f_1': 'INT',
        'past_bris_pace_6f_2': 'INT',
        'past_bris_pace_6f_3': 'INT',
        'past_bris_pace_6f_4': 'INT',
        'past_bris_pace_6f_5': 'INT',
        'past_bris_pace_6f_6': 'INT',
        'past_bris_pace_6f_7': 'INT',
        'past_bris_pace_6f_8': 'INT',
        'past_bris_pace_6f_9': 'INT',
        'past_bris_pace_6f_10': 'INT',

        'past_bris_pace_8f_1': 'INT',
        'past_bris_pace_8f_2': 'INT',
        'past_bris_pace_8f_3': 'INT',
        'past_bris_pace_8f_4': 'INT',
        'past_bris_pace_8f_5': 'INT',
        'past_bris_pace_8f_6': 'INT',
        'past_bris_pace_8f_7': 'INT',
        'past_bris_pace_8f_8': 'INT',
        'past_bris_pace_8f_9': 'INT',
        'past_bris_pace_8f_10': 'INT',

        'past_bris_pace_10f_1': 'INT',
        'past_bris_pace_10f_2': 'INT',
        'past_bris_pace_10f_3': 'INT',
        'past_bris_pace_10f_4': 'INT',
        'past_bris_pace_10f_5': 'INT',
        'past_bris_pace_10f_6': 'INT',
        'past_bris_pace_10f_7': 'INT',
        'past_bris_pace_10f_8': 'INT',
        'past_bris_pace_10f_9': 'INT',
        'past_bris_pace_10f_10': 'INT',

        'past_bris_pace_late_1': 'INT',
        'past_bris_pace_late_2': 'INT',
        'past_bris_pace_late_3': 'INT',
        'past_bris_pace_late_4': 'INT',
        'past_bris_pace_late_5': 'INT',
        'past_bris_pace_late_6': 'INT',
        'past_bris_pace_late_7': 'INT',
        'past_bris_pace_late_8': 'INT',
        'past_bris_pace_late_9': 'INT',
        'past_bris_pace_late_10': 'INT',

        #      BRIS Speed Rating
        'past_bris_speed_rating_1': 'INT',
        'past_bris_speed_rating_2': 'INT',
        'past_bris_speed_rating_3': 'INT',
        'past_bris_speed_rating_4': 'INT',
        'past_bris_speed_rating_5': 'INT',
        'past_bris_speed_rating_6': 'INT',
        'past_bris_speed_rating_7': 'INT',
        'past_bris_speed_rating_8': 'INT',
        'past_bris_speed_rating_9': 'INT',
        'past_bris_speed_rating_10': 'INT',

        ##      Speed rating
        'past_speed_rating_1': 'INT',
        'past_speed_rating_2': 'INT',
        'past_speed_rating_3': 'INT',
        'past_speed_rating_4': 'INT',
        'past_speed_rating_5': 'INT',
        'past_speed_rating_6': 'INT',
        'past_speed_rating_7': 'INT',
        'past_speed_rating_8': 'INT',
        'past_speed_rating_9': 'INT',
        'past_speed_rating_10': 'INT',

        ##      Track Variant
        'past_track_variant_1': 'INT',
        'past_track_variant_2': 'INT',
        'past_track_variant_3': 'INT',
        'past_track_variant_4': 'INT',
        'past_track_variant_5': 'INT',
        'past_track_variant_6': 'INT',
        'past_track_variant_7': 'INT',
        'past_track_variant_8': 'INT',
        'past_track_variant_9': 'INT',
        'past_track_variant_10': 'INT',

        ## Past Fractions (seconds and hundreths)

        'past_fraction_2f_1': 'FLOAT',
        'past_fraction_2f_2': 'FLOAT',
        'past_fraction_2f_3': 'FLOAT',
        'past_fraction_2f_4': 'FLOAT',
        'past_fraction_2f_5': 'FLOAT',
        'past_fraction_2f_6': 'FLOAT',
        'past_fraction_2f_7': 'FLOAT',
        'past_fraction_2f_8': 'FLOAT',
        'past_fraction_2f_9': 'FLOAT',
        'past_fraction_2f_10': 'FLOAT',

        'past_fraction_3f_1': 'FLOAT',
        'past_fraction_3f_2': 'FLOAT',
        'past_fraction_3f_3': 'FLOAT',
        'past_fraction_3f_4': 'FLOAT',
        'past_fraction_3f_5': 'FLOAT',
        'past_fraction_3f_6': 'FLOAT',
        'past_fraction_3f_7': 'FLOAT',
        'past_fraction_3f_8': 'FLOAT',
        'past_fraction_3f_9': 'FLOAT',
        'past_fraction_3f_10': 'FLOAT',

        'past_fraction_4f_1': 'FLOAT',
        'past_fraction_4f_2': 'FLOAT',
        'past_fraction_4f_3': 'FLOAT',
        'past_fraction_4f_4': 'FLOAT',
        'past_fraction_4f_5': 'FLOAT',
        'past_fraction_4f_6': 'FLOAT',
        'past_fraction_4f_7': 'FLOAT',
        'past_fraction_4f_8': 'FLOAT',
        'past_fraction_4f_9': 'FLOAT',
        'past_fraction_4f_10': 'FLOAT',

        'past_fraction_5f_1': 'FLOAT',
        'past_fraction_5f_2': 'FLOAT',
        'past_fraction_5f_3': 'FLOAT',
        'past_fraction_5f_4': 'FLOAT',
        'past_fraction_5f_5': 'FLOAT',
        'past_fraction_5f_6': 'FLOAT',
        'past_fraction_5f_7': 'FLOAT',
        'past_fraction_5f_8': 'FLOAT',
        'past_fraction_5f_9': 'FLOAT',
        'past_fraction_5f_10': 'FLOAT',

        'past_fraction_6f_1': 'FLOAT',
        'past_fraction_6f_2': 'FLOAT',
        'past_fraction_6f_3': 'FLOAT',
        'past_fraction_6f_4': 'FLOAT',
        'past_fraction_6f_5': 'FLOAT',
        'past_fraction_6f_6': 'FLOAT',
        'past_fraction_6f_7': 'FLOAT',
        'past_fraction_6f_8': 'FLOAT',
        'past_fraction_6f_9': 'FLOAT',
        'past_fraction_6f_10': 'FLOAT',

        'past_fraction_7f_1': 'FLOAT',
        'past_fraction_7f_2': 'FLOAT',
        'past_fraction_7f_3': 'FLOAT',
        'past_fraction_7f_4': 'FLOAT',
        'past_fraction_7f_5': 'FLOAT',
        'past_fraction_7f_6': 'FLOAT',
        'past_fraction_7f_7': 'FLOAT',
        'past_fraction_7f_8': 'FLOAT',
        'past_fraction_7f_9': 'FLOAT',
        'past_fraction_7f_10': 'FLOAT',

        'past_fraction_8f_1': 'FLOAT',
        'past_fraction_8f_2': 'FLOAT',
        'past_fraction_8f_3': 'FLOAT',
        'past_fraction_8f_4': 'FLOAT',
        'past_fraction_8f_5': 'FLOAT',
        'past_fraction_8f_6': 'FLOAT',
        'past_fraction_8f_7': 'FLOAT',
        'past_fraction_8f_8': 'FLOAT',
        'past_fraction_8f_9': 'FLOAT',
        'past_fraction_8f_10': 'FLOAT',

        'past_fraction_10f_1': 'FLOAT',
        'past_fraction_10f_2': 'FLOAT',
        'past_fraction_10f_3': 'FLOAT',
        'past_fraction_10f_4': 'FLOAT',
        'past_fraction_10f_5': 'FLOAT',
        'past_fraction_10f_6': 'FLOAT',
        'past_fraction_10f_7': 'FLOAT',
        'past_fraction_10f_8': 'FLOAT',
        'past_fraction_10f_9': 'FLOAT',
        'past_fraction_10f_10': 'FLOAT',

        'past_fraction_12f_1': 'FLOAT',
        'past_fraction_12f_2': 'FLOAT',
        'past_fraction_12f_3': 'FLOAT',
        'past_fraction_12f_4': 'FLOAT',
        'past_fraction_12f_5': 'FLOAT',
        'past_fraction_12f_6': 'FLOAT',
        'past_fraction_12f_7': 'FLOAT',
        'past_fraction_12f_8': 'FLOAT',
        'past_fraction_12f_9': 'FLOAT',
        'past_fraction_12f_10': 'FLOAT',

        'past_fraction_14f_1': 'FLOAT',
        'past_fraction_14f_2': 'FLOAT',
        'past_fraction_14f_3': 'FLOAT',
        'past_fraction_14f_4': 'FLOAT',
        'past_fraction_14f_5': 'FLOAT',
        'past_fraction_14f_6': 'FLOAT',
        'past_fraction_14f_7': 'FLOAT',
        'past_fraction_14f_8': 'FLOAT',
        'past_fraction_14f_9': 'FLOAT',
        'past_fraction_14f_10': 'FLOAT',

        'past_fraction_16f_1': 'FLOAT',
        'past_fraction_16f_2': 'FLOAT',
        'past_fraction_16f_3': 'FLOAT',
        'past_fraction_16f_4': 'FLOAT',
        'past_fraction_16f_5': 'FLOAT',
        'past_fraction_16f_6': 'FLOAT',
        'past_fraction_16f_7': 'FLOAT',
        'past_fraction_16f_8': 'FLOAT',
        'past_fraction_16f_9': 'FLOAT',
        'past_fraction_16f_10': 'FLOAT',

         ##     Fractions #1, #2, #3
        'past_fraction_first_1': 'FLOAT',
        'past_fraction_first_2': 'FLOAT',
        'past_fraction_first_3': 'FLOAT',
        'past_fraction_first_4': 'FLOAT',
        'past_fraction_first_5': 'FLOAT',
        'past_fraction_first_6': 'FLOAT',
        'past_fraction_first_7': 'FLOAT',
        'past_fraction_first_8': 'FLOAT',
        'past_fraction_first_9': 'FLOAT',
        'past_fraction_first_10': 'FLOAT',

        'past_fraction_second_1': 'FLOAT',
        'past_fraction_second_2': 'FLOAT',
        'past_fraction_second_3': 'FLOAT',
        'past_fraction_second_4': 'FLOAT',
        'past_fraction_second_5': 'FLOAT',
        'past_fraction_second_6': 'FLOAT',
        'past_fraction_second_7': 'FLOAT',
        'past_fraction_second_8': 'FLOAT',
        'past_fraction_second_9': 'FLOAT',
        'past_fraction_second_10': 'FLOAT',

        'past_fraction_third_1': 'FLOAT',
        'past_fraction_third_2': 'FLOAT',
        'past_fraction_third_3': 'FLOAT',
        'past_fraction_third_4': 'FLOAT',
        'past_fraction_third_5': 'FLOAT',
        'past_fraction_third_6': 'FLOAT',
        'past_fraction_third_7': 'FLOAT',
        'past_fraction_third_8': 'FLOAT',
        'past_fraction_third_9': 'FLOAT',
        'past_fraction_third_10': 'FLOAT',

        #      Final time
        'past_final_time_1': 'FLOAT',
        'past_final_time_2': 'FLOAT',
        'past_final_time_3': 'FLOAT',
        'past_final_time_4': 'FLOAT',
        'past_final_time_5': 'FLOAT',
        'past_final_time_6': 'FLOAT',
        'past_final_time_7': 'FLOAT',
        'past_final_time_8': 'FLOAT',
        'past_final_time_9': 'FLOAT',
        'past_final_time_10': 'FLOAT',

        #      Claimed code
        'past_claimed_code_1': 'INT',
        'past_claimed_code_2': 'INT',
        'past_claimed_code_3': 'INT',
        'past_claimed_code_4': 'INT',
        'past_claimed_code_5': 'INT',
        'past_claimed_code_6': 'INT',
        'past_claimed_code_7': 'INT',
        'past_claimed_code_8': 'INT',
        'past_claimed_code_9': 'INT',
        'past_claimed_code_10': 'INT',

        ##      Past Trainer (when available) and Jockey
        'past_trainer_1': 'VARCHAR(255)',
        'past_trainer_2': 'VARCHAR(255)',
        'past_trainer_3': 'VARCHAR(255)',
        'past_trainer_4': 'VARCHAR(255)',
        'past_trainer_5': 'VARCHAR(255)',
        'past_trainer_6': 'VARCHAR(255)',
        'past_trainer_7': 'VARCHAR(255)',
        'past_trainer_8': 'VARCHAR(255)',
        'past_trainer_9': 'VARCHAR(255)',
        'past_trainer_10': 'VARCHAR(255)',

        'past_jockey_1': 'VARCHAR(255)',
        'past_jockey_2': 'VARCHAR(255)',
        'past_jockey_3': 'VARCHAR(255)',
        'past_jockey_4': 'VARCHAR(255)',
        'past_jockey_5': 'VARCHAR(255)',
        'past_jockey_6': 'VARCHAR(255)',
        'past_jockey_7': 'VARCHAR(255)',
        'past_jockey_8': 'VARCHAR(255)',
        'past_jockey_9': 'VARCHAR(255)',
        'past_jockey_10': 'VARCHAR(255)',

        ##      Apprentice weight allowance (if any)
        'past_weight_allowance_1': 'INT',
        'past_weight_allowance_2': 'INT',
        'past_weight_allowance_3': 'INT',
        'past_weight_allowance_4': 'INT',
        'past_weight_allowance_5': 'INT',
        'past_weight_allowance_6': 'INT',
        'past_weight_allowance_7': 'INT',
        'past_weight_allowance_8': 'INT',
        'past_weight_allowance_9': 'INT',
        'past_weight_allowance_10': 'INT',

        ##      Race type
        'past_race_type_1': 'VARCHAR(255)',
        'past_race_type_2': 'VARCHAR(255)',
        'past_race_type_3': 'VARCHAR(255)',
        'past_race_type_4': 'VARCHAR(255)',
        'past_race_type_5': 'VARCHAR(255)',
        'past_race_type_6': 'VARCHAR(255)',
        'past_race_type_7': 'VARCHAR(255)',
        'past_race_type_8': 'VARCHAR(255)',
        'past_race_type_9': 'VARCHAR(255)',
        'past_race_type_10': 'VARCHAR(255)',
                                            ##                                              C- 4 year olds
        ##      Age and sex restrictions                                                    D- 5 year olds
        'past_age_sex_restrictions_1': 'VARCHAR(255)',
        'past_age_sex_restrictions_2': 'VARCHAR(255)',
        'past_age_sex_restrictions_3': 'VARCHAR(255)',
        'past_age_sex_restrictions_4': 'VARCHAR(255)',
        'past_age_sex_restrictions_5': 'VARCHAR(255)',
        'past_age_sex_restrictions_6': 'VARCHAR(255)',
        'past_age_sex_restrictions_7': 'VARCHAR(255)',
        'past_age_sex_restrictions_8': 'VARCHAR(255)',
        'past_age_sex_restrictions_9': 'VARCHAR(255)',
        'past_age_sex_restrictions_10': 'VARCHAR(255)',
                                            ##                                              N - No Sex Restrictions
                                            ##                                              M - Mares and Fillies Only
                                            ##                                              C - Colts or Geldings Only
                                            ##                                              F - Fillies Only
                                            ##      E.g.: 'BON' - means a '3 year olds only,'  no sex restrictions

        ##      Statebred flag
        'past_statebred_flag_1': 'INT',
        'past_statebred_flag_2': 'INT',
        'past_statebred_flag_3': 'INT',
        'past_statebred_flag_4': 'INT',
        'past_statebred_flag_5': 'INT',
        'past_statebred_flag_6': 'INT',
        'past_statebred_flag_7': 'INT',
        'past_statebred_flag_8': 'INT',
        'past_statebred_flag_9': 'INT',
        'past_statebred_flag_10': 'INT',

        ##      Restricted/Qualified flag
        'past_restricted_or_qualified_1': 'VARCHAR(255)',
        'past_restricted_or_qualified_2': 'VARCHAR(255)',
        'past_restricted_or_qualified_3': 'VARCHAR(255)',
        'past_restricted_or_qualified_4': 'VARCHAR(255)',
        'past_restricted_or_qualified_5': 'VARCHAR(255)',
        'past_restricted_or_qualified_6': 'VARCHAR(255)',
        'past_restricted_or_qualified_7': 'VARCHAR(255)',
        'past_restricted_or_qualified_8': 'VARCHAR(255)',
        'past_restricted_or_qualified_9': 'VARCHAR(255)',
        'past_restricted_or_qualified_10': 'VARCHAR(255)',

        ##      Favorite indicator
        'past_favorite_flag_1': 'INT',
        'past_favorite_flag_2': 'INT',
        'past_favorite_flag_3': 'INT',
        'past_favorite_flag_4': 'INT',
        'past_favorite_flag_5': 'INT',
        'past_favorite_flag_6': 'INT',
        'past_favorite_flag_7': 'INT',
        'past_favorite_flag_8': 'INT',
        'past_favorite_flag_9': 'INT',
        'past_favorite_flag_10': 'INT',

        ##      Front bandages indicator
        'past_front_wraps_1': 'INT',
        'past_front_wraps_2': 'INT',
        'past_front_wraps_3': 'INT',
        'past_front_wraps_4': 'INT',
        'past_front_wraps_5': 'INT',
        'past_front_wraps_6': 'INT',
        'past_front_wraps_7': 'INT',
        'past_front_wraps_8': 'INT',
        'past_front_wraps_9': 'INT',
        'past_front_wraps_10': 'INT',

        ##      Trainer and Jockey stats Current/Past Year
        'trainer_current_year_starts': 'INT',
        'trainer_current_year_wins': 'INT',
        'trainer_current_year_places': 'INT',
        'trainer_current_year_shows': 'INT',
        'trainer_current_year_roi': 'FLOAT',

        'trainer_past_year_starts': 'INT',
        'trainer_past_year_wins': 'INT',
        'trainer_past_year_places': 'INT',
        'trainer_past_year_shows': 'INT',
        'trainer_past_year_roi': 'FLOAT',

        'jockey_current_year_starts': 'INT',
        'jockey_current_year_wins': 'INT',
        'jockey_current_year_places': 'INT',
        'jockey_current_year_shows': 'INT',
        'jockey_current_year_roi': 'FLOAT',

        'jockey_past_year_starts': 'INT',
        'jockey_past_year_wins': 'INT',
        'jockey_past_year_places': 'INT',
        'jockey_past_year_shows': 'INT',
        'jockey_past_year_roi': 'FLOAT',

        ##      BRIS Speed Par for Class Level of last 10 races
        'past_bris_par_for_class_1': 'INT',
        'past_bris_par_for_class_2': 'INT',
        'past_bris_par_for_class_3': 'INT',
        'past_bris_par_for_class_4': 'INT',
        'past_bris_par_for_class_5': 'INT',
        'past_bris_par_for_class_6': 'INT',
        'past_bris_par_for_class_7': 'INT',
        'past_bris_par_for_class_8': 'INT',
        'past_bris_par_for_class_9': 'INT',
        'past_bris_par_for_class_10': 'INT',

        ##      Sire stud fee (current)
        'sire_stud_fee_current': 'INT',

        ##      Best BRIS Speeds
        'best_bris_speed_fast': 'INT',
        'best_bris_speed_turf': 'INT',
        'best_bris_speed_off_track': 'INT',
        'best_bris_speed_at_distance': 'INT',

        ## Bar Shoe WHAT DOES THIS MEAN?
        'past_bar_shoe_1': 'INT',
        'past_bar_shoe_2': 'INT',
        'past_bar_shoe_3': 'INT',
        'past_bar_shoe_4': 'INT',
        'past_bar_shoe_5': 'INT',
        'past_bar_shoe_6': 'INT',
        'past_bar_shoe_7': 'INT',
        'past_bar_shoe_8': 'INT',
        'past_bar_shoe_9': 'INT',
        'past_bar_shoe_10': 'INT',

        ##      Company line codes
        'past_company_line_1': 'VARCHAR(255)',
        'past_company_line_2': 'VARCHAR(255)',
        'past_company_line_3': 'VARCHAR(255)',
        'past_company_line_4': 'VARCHAR(255)',
        'past_company_line_5': 'VARCHAR(255)',
        'past_company_line_6': 'VARCHAR(255)',
        'past_company_line_7': 'VARCHAR(255)',
        'past_company_line_8': 'VARCHAR(255)',
        'past_company_line_9': 'VARCHAR(255)',
        'past_company_line_10': 'VARCHAR(255)',

        ##      High and Low claiming price of race
        'past_low_claiming_price_1': 'INT',
        'past_low_claiming_price_2': 'INT',
        'past_low_claiming_price_3': 'INT',
        'past_low_claiming_price_4': 'INT',
        'past_low_claiming_price_5': 'INT',
        'past_low_claiming_price_6': 'INT',
        'past_low_claiming_price_7': 'INT',
        'past_low_claiming_price_8': 'INT',
        'past_low_claiming_price_9': 'INT',
        'past_low_claiming_price_10': 'INT',

        'past_high_claiming_price_1': 'INT',
        'past_high_claiming_price_2': 'INT',
        'past_high_claiming_price_3': 'INT',
        'past_high_claiming_price_4': 'INT',
        'past_high_claiming_price_5': 'INT',
        'past_high_claiming_price_6': 'INT',
        'past_high_claiming_price_7': 'INT',
        'past_high_claiming_price_8': 'INT',
        'past_high_claiming_price_9': 'INT',
        'past_high_claiming_price_10': 'INT',

        ##      Aution price and when/when sold at auction
        'auction_price': 'INT',
        'auction_where_when': 'VARCHAR(255)',

        ##      Code for prior 10 starts
        'past_start_code_1': 'VARCHAR(255)',
        'past_start_code_2': 'VARCHAR(255)',
        'past_start_code_3': 'VARCHAR(255)',
        'past_start_code_4': 'VARCHAR(255)',
        'past_start_code_5': 'VARCHAR(255)',
        'past_start_code_6': 'VARCHAR(255)',
        'past_start_code_7': 'VARCHAR(255)',
        'past_start_code_8': 'VARCHAR(255)',
        'past_start_code_9': 'VARCHAR(255)',
        'past_start_code_10': 'VARCHAR(255)',

        ##      BRIS Pedigree Ratings
        'bris_pedigree_rating_dirt': 'VARCHAR(255)',
        'bris_pedigree_rating_mud': 'VARCHAR(255)',
        'bris_pedigree_rating_turf': 'VARCHAR(255)',
        'bris_pedigree_rating_at_distance': 'VARCHAR(255)',

        ##      Claimed from and trainer siwtches
        'past_claim_trainer_switch_date_1': 'VARCHAR(255)',
        'past_claim_trainer_switch_date_2': 'VARCHAR(255)',
        'past_claim_trainer_switch_date_3': 'VARCHAR(255)',
        'past_claim_trainer_switch_date_4': 'VARCHAR(255)',
        'past_claim_trainer_switch_date_5': 'VARCHAR(255)',
        'past_claim_trainer_switch_date_6': 'VARCHAR(255)',
        'past_claim_trainer_switch_date_7': 'VARCHAR(255)',
        'past_claim_trainer_switch_date_8': 'VARCHAR(255)',
        'past_claim_trainer_switch_date_9': 'VARCHAR(255)',
        'past_claim_trainer_switch_date_10': 'VARCHAR(255)',

        ##      Claimed from and trainer switches
        'past_claim_trainer_switch_1_1': 'INT',
        'past_claim_trainer_switch_1_2': 'INT',
        'past_claim_trainer_switch_1_3': 'INT',
        'past_claim_trainer_switch_1_4': 'INT',
        'past_claim_trainer_switch_1_5': 'INT',
        'past_claim_trainer_switch_1_6': 'INT',
        'past_claim_trainer_switch_1_7': 'INT',
        'past_claim_trainer_switch_1_8': 'INT',
        'past_claim_trainer_switch_1_9': 'INT',
        'past_claim_trainer_switch_1_10': 'INT',

        ##      Claimed from and trainer switches
        'past_claim_trainer_switch_2_1': 'INT',
        'past_claim_trainer_switch_2_2': 'INT',
        'past_claim_trainer_switch_2_3': 'INT',
        'past_claim_trainer_switch_2_4': 'INT',
        'past_claim_trainer_switch_2_5': 'INT',
        'past_claim_trainer_switch_2_6': 'INT',
        'past_claim_trainer_switch_2_7': 'INT',
        'past_claim_trainer_switch_2_8': 'INT',
        'past_claim_trainer_switch_2_9': 'INT',
        'past_claim_trainer_switch_2_10': 'INT',

        ##      Claimed from and trainer switches
        'past_claim_trainer_switch_3_1': 'INT',
        'past_claim_trainer_switch_3_2': 'INT',
        'past_claim_trainer_switch_3_3': 'INT',
        'past_claim_trainer_switch_3_4': 'INT',
        'past_claim_trainer_switch_3_5': 'INT',
        'past_claim_trainer_switch_3_6': 'INT',
        'past_claim_trainer_switch_3_7': 'INT',
        'past_claim_trainer_switch_3_8': 'INT',
        'past_claim_trainer_switch_3_9': 'INT',
        'past_claim_trainer_switch_3_10': 'INT',

        ##      Claimed from and trainer switches
        'past_claim_trainer_switch_4_1': 'INT',
        'past_claim_trainer_switch_4_2': 'INT',
        'past_claim_trainer_switch_4_3': 'INT',
        'past_claim_trainer_switch_4_4': 'INT',
        'past_claim_trainer_switch_4_5': 'INT',
        'past_claim_trainer_switch_4_6': 'INT',
        'past_claim_trainer_switch_4_7': 'INT',
        'past_claim_trainer_switch_4_8': 'INT',
        'past_claim_trainer_switch_4_9': 'INT',
        'past_claim_trainer_switch_4_10': 'INT',

        ##      Claimed from and trainer switches
        'past_claim_trainer_switch_5_1': 'INT',
        'past_claim_trainer_switch_5_2': 'INT',
        'past_claim_trainer_switch_5_3': 'INT',
        'past_claim_trainer_switch_5_4': 'INT',
        'past_claim_trainer_switch_5_5': 'INT',
        'past_claim_trainer_switch_5_6': 'INT',
        'past_claim_trainer_switch_5_7': 'INT',
        'past_claim_trainer_switch_5_8': 'INT',
        'past_claim_trainer_switch_5_9': 'INT',
        'past_claim_trainer_switch_5_10': 'INT',


        ##      Best BRIS Speeds: Life, Most recent year horse ran, 2d most recent year horse ran, today's track
        'best_bris_speed_life': 'INT',
        'best_bris_speed_recent_year': 'INT',
        'best_bris_speed_2d_recent_year': 'INT',
        'best_bris_speed_todays_track': 'INT',

        ##      Fast Dirt stats
        'fast_dirt_starts': 'INT',
        'fast_dirt_wins': 'INT',
        'fast_dirt_places': 'INT',
        'fast_dirt_shows': 'INT',
        'fast_dirt_earned': 'INT',

        ## Key Traininer stat Category 1

        'trainer_stat_1_name': 'VARCHAR(255)',
        'trainer_stat_1_starts': 'INT',
        'trainer_stat_1_win_percent': 'FLOAT',
        'trainer_stat_1_itm_percent': 'FLOAT',
        'trainer_stat_1_roi': 'FLOAT',

        ## Key Traininer stat Category 2

        'trainer_stat_2_name': 'VARCHAR(255)',
        'trainer_stat_2_starts': 'INT',
        'trainer_stat_2_win_percent': 'FLOAT',
        'trainer_stat_2_itm_percent': 'FLOAT',
        'trainer_stat_2_roi': 'FLOAT',

        ## Key Traininer stat Category 3

        'trainer_stat_3_name': 'VARCHAR(255)',
        'trainer_stat_3_starts': 'INT',
        'trainer_stat_3_win_percent': 'FLOAT',
        'trainer_stat_3_itm_percent': 'FLOAT',
        'trainer_stat_3_roi': 'FLOAT',

        ## Key Traininer stat Category 4

        'trainer_stat_4_name': 'VARCHAR(255)',
        'trainer_stat_4_starts': 'INT',
        'trainer_stat_4_win_percent': 'FLOAT',
        'trainer_stat_4_itm_percent': 'FLOAT',
        'trainer_stat_4_roi': 'FLOAT',

        ## Key Traininer stat Category 5

        'trainer_stat_5_name': 'VARCHAR(255)',
        'trainer_stat_5_starts': 'INT',
        'trainer_stat_5_win_percent': 'FLOAT',
        'trainer_stat_5_itm_percent': 'FLOAT',
        'trainer_stat_5_roi': 'FLOAT',

        ## Key Traininer stat Category 6

        'trainer_stat_6_name': 'VARCHAR(255)',
        'trainer_stat_6_starts': 'INT',
        'trainer_stat_6_win_percent': 'FLOAT',
        'trainer_stat_6_itm_percent': 'FLOAT',
        'trainer_stat_6_roi': 'FLOAT',

        ##      JKY @ Distance/ Jky on Turf stats

        'jockey_at_distance_on_turf_label': 'VARCHAR(255)',
        'jockey_at_distance_on_turf_starts': 'INT',
        'jockey_at_distance_on_turf_wins': 'INT',
        'jockey_at_distance_on_turf_places': 'INT',
        'jockey_at_distance_on_turf_shows': 'INT',
        'jockey_at_distance_on_turf_roi': 'FLOAT',
        'jockey_at_distance_on_turf_earnings': 'INT',

        ## Post times(by region)

        'post_times_by_region': 'VARCHAR(255)',

        ##      Extended Start Comment
        'past_extended_start_comment_1': 'VARCHAR(255)',
        'past_extended_start_comment_2': 'VARCHAR(255)',
        'past_extended_start_comment_3': 'VARCHAR(255)',
        'past_extended_start_comment_4': 'VARCHAR(255)',
        'past_extended_start_comment_5': 'VARCHAR(255)',
        'past_extended_start_comment_6': 'VARCHAR(255)',
        'past_extended_start_comment_7': 'VARCHAR(255)',
        'past_extended_start_comment_8': 'VARCHAR(255)',
        'past_extended_start_comment_9': 'VARCHAR(255)',
        'past_extended_start_comment_10': 'VARCHAR(255)',

        ##      'Sealed' track indicator
        'past_sealed_track_indicator_1': 'INT',
        'past_sealed_track_indicator_2': 'INT',
        'past_sealed_track_indicator_3': 'INT',
        'past_sealed_track_indicator_4': 'INT',
        'past_sealed_track_indicator_5': 'INT',
        'past_sealed_track_indicator_6': 'INT',
        'past_sealed_track_indicator_7': 'INT',
        'past_sealed_track_indicator_8': 'INT',
        'past_sealed_track_indicator_9': 'INT',
        'past_sealed_track_indicator_10': 'INT',

        ##      Prev. All-Weather Sureface Flag
        'past_all_weather_flag_1': 'INT',
        'past_all_weather_flag_2': 'INT',
        'past_all_weather_flag_3': 'INT',
        'past_all_weather_flag_4': 'INT',
        'past_all_weather_flag_5': 'INT',
        'past_all_weather_flag_6': 'INT',
        'past_all_weather_flag_7': 'INT',
        'past_all_weather_flag_8': 'INT',
        'past_all_weather_flag_9': 'INT',
        'past_all_weather_flag_10': 'INT',

        ##      Trainer/Jockey combo stats (meet)
        'TJ_combo_starts': 'INT',
        'TJ_combo_wins': 'INT',
        'TJ_combo_places': 'INT',
        'TJ_combo_shows': 'INT',
        'TJ_combo_roi': 'FLOAT',

        ##      Post time (PAcific military time) '0300' for 3am pacific time
        'post_time_pacific_military': 'VARCHAR(255)',

        ##      Equibase abbreviated race conditions
        'past_equibase_race_conditions_1': 'VARCHAR(255)',
        'past_equibase_race_conditions_2': 'VARCHAR(255)',
        'past_equibase_race_conditions_3': 'VARCHAR(255)',
        'past_equibase_race_conditions_4': 'VARCHAR(255)',
        'past_equibase_race_conditions_5': 'VARCHAR(255)',
        'past_equibase_race_conditions_6': 'VARCHAR(255)',
        'past_equibase_race_conditions_7': 'VARCHAR(255)',
        'past_equibase_race_conditions_8': 'VARCHAR(255)',
        'past_equibase_race_conditions_9': 'VARCHAR(255)',
        'past_equibase_race_conditions_10': 'VARCHAR(255)',

        'equibase_race_conditions': 'VARCHAR(255)',
    },
}