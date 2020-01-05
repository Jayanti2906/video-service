Model Architecture planning 

 Membership 
     -slug
     -type( free, pro, enterprise)
     -price
     -stripe plan id

 UserMembership
     -user                   (foreignkey to default user)
     -stripe customer id      
     -membership type        (foreignkey to membership)
     
 Subscription 
     -user membership
     -stripe subscription id  (foreign key to the UserMembership)
     -active

 Course    
     -slug
     -title
     -description
     -allowed membership       (ManyToManyField to the Membership)

 Lesson    
     -slug
     -title
     -Course                   (foreignkey to Course)
     -position
     -video
     -thumbnail

