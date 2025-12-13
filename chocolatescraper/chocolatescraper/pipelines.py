# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class ChocolatescraperPipeline:
    def process_item(self, item, spider):
        return item

class GbpToRuppesPipeline:
    def __init__(self):
        self.gbptorupperate = 120.88
        
    def process_item(self,item,spider):
        adapter = ItemAdapter(item)
        if(adapter.get('price')):
            adapter['price']=float(adapter['price'])*self.gbptorupperate
        else:
            raise DropItem(f"Missing price of item {item}")
        return item

class RemoveDuplicatePipeline:
    def __init__(self):
        self.name_seen = set()

    def process_item(self,item,spider):
        adapter = ItemAdapter(item)
        title = adapter['name']
        if(title in self.name_seen):
            raise DropItem(f"already present in set {item}")
        else:
            self.name_seen.add(item)
            return item