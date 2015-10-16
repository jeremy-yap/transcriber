import os

from django.core.management.base import BaseCommand  
from ...models import Audio

class Command(BaseCommand):

	def handle(self, *args, **options):
		audioInfo = [
			[1, 'cantonese_141015_367259-15', '256662351261343423115414'],
			[2, 'cantonese_140927_363450-6', '3366255344362253126114436'],
			[3, 'cantonese_140916_361200-30', '23535636144362463323136516'],
			[4, 'cantonese_140927_363450-5', '444215614163556266422313'],
			[5, 'cantonese_140916_361200-13', '626354115362633631651243432'],
			[6, 'cantonese_140916_361200-22', '146331626251131425214451'],
			[7, 'cantonese_140925_363090-6', '364244156135441145351262'],
			[8, 'cantonese_140926_363178-21', '44541162263564363256112'],
			[9, 'cantonese_140926_363298-6', '1634143245631232565633'],
			[10, 'cantonese_140927_363450-1', '643626135363425514113642'],
			[11, 'cantonese_140927_363450-24', '126556313235264344113'],
			[12, 'cantonese_141015_367259-23', '43411561346342544266561312'],
		]

		for i in audioInfo:
			Audio.objects.update_or_create(
				id = i[0],
					defaults={
					'fileName' : i[1],
					'numSegments' : len(i[2]),
					'answer' : i[2],
				}
			)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9 之后嘅时间人数可能会达到三位数㗎佢地强调呀将
# 10 达成嘅重行定居协议正被扣留喺鲁鲁机留中心嘅难民可
# 11
# 12