(define (domain nao-world)
	(:requirements :typing :durative-actions)
	(:types direction thing location - object
		robot box ball - thing)
	(:predicates    (HandEmpty ?r - robot)
	        	(clear ?l - location)
			(Holding ?r - robot ?b - box)
			(at ?t - thing ?l - location)
			(MOVE-DIR ?l1 ?l2 - location ?d - direction))


	(:durative-action move
	   :parameters (?r - robot ?from ?to - location ?dir - direction)
	   :duration  (= ?duration 1)
	   :condition (and (at start (at ?r ?from))
		           (at start (clear ?to))
		           (over all (MOVE-DIR ?from ?to ?dir))
		           )
	   :effect    (and (at start (not (at ?r ?from)))
		           (at start (not (clear ?to)))
		           (at end (at ?r ?to))
		           (at end (clear ?from))
		           )
	   )


	(:durative-action kick
		:parameters (?r - robot ?b - ball ?l1 ?l2 ?l3 - location ?d1 - direction)
		:duration (= ?duration 1)
		:condition (and (at start (at ?b ?l2))
				(at start (at ?r ?l1)) 
				(at start (clear ?l3))
				(at start (MOVE-DIR ?l1 ?l2 ?d1)) 
				(at start (MOVE-DIR ?l2 ?l3 ?d1)) 
				)
		:effect	(and (at end (not (at ?b ?l2)))
			     (at end (at ?b ?l3)) 
			     (at end (not (clear ?l3))) 
			     (at end(clear ?l2)) 
			     ) 
		)

	(:durative-action pick-up
		:parameters (?r - robot ?b - box ?l1 ?l2 - location ?d - direction)
		:duration (= ?duration 3)
		:condition (and (at start (HandEmpty ?r)) 
				(at start (at ?r ?l1)) 
				(at start (at ?b ?l2)) 
				(at start (MOVE-DIR ?l1 ?l2 ?d)) 
				)
		:effect (and (at end (not (HandEmpty ?r)))
			     (at end (not (at ?b ?l2)))
			     (at end (clear ?l2)) 
                             (at end (Holding ?r ?b)) 
			     )
		)

	(:durative-action drop
		:parameters (?r - robot ?b - box ?l1 ?l2 - location ?d - direction)
		:duration (= ?duration 3)
		:condition (and (at start (not (HandEmpty ?r)))
				(at start (at ?r ?l1)) 
				(at start (Holding ?r ?b)) 
				(at start (clear ?l2)) 
				(at start (MOVE-DIR ?l1 ?l2 ?d)) 
				)
		:effect (and (at end (HandEmpty ?r)) 
			     (at end (at ?b ?l2)) 
			     (at end (not (Holding ?r ?b))) 
			     (at end (not (clear ?l2))) 
			)
		)
	)
