# from mentorsforall.models import Profile
# from collections import defaultdict
#
# # # this algorithm gets all matching profiles
# # def get_matches(this_profile_id):
# #
# # 	# get the profile of id
# # 	this_profile = Profile.objects.get(id = this_profile_id)
# # 	# the profile hobbies
# # 	# this_profile_hobbies = this_profile.hobbies.all()
# #
# # 	# create a defaultdict which creates an empty list for each key accessed
# # 	matched_profiles = defaultdict(list)
# #
# # 	# for each hobby
# # 	# for h in this_profile_hobbies:
# # 	# iterate over matching profiles, excluding this one
# # 	for matching_profile in h.hobby_users.all().exclude(id=this_profile_id):
# # 		# add to the list
# # 		matched_profiles[matching_profile].append(h)
# #
# # 	# # sort them by number of hobbies in common
# # 	# ranked = [ (key, len(value), value) for key, value in matched_profiles.items() ]
# # 	# ranked = sorted(ranked, reverse=True, key=lambda x: x[1])
# #
# # 	return ranked
#
# def filtering_results(this_profile_id, currentmatches):
#     this_profile = Profile.objects.get(id = this_profile_id)
