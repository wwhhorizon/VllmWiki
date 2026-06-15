# vllm-project/vllm#2129: Output changes after Prefix warmup.

| 字段 | 值 |
| --- | --- |
| Issue | [#2129](https://github.com/vllm-project/vllm/issues/2129) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Output changes after Prefix warmup.

### Issue 正文摘录

@caoshiyi I think ouput should be equal when setting prefix for the first time and after. But my test shows that output will changes after you first set this prefix. In addention, output of without prefix will also affected when batchsize is too big(seems when requests can't be push into scheduler.running at once) I have set temperature=0 to obtain a fixed output. Model: llama-7b, prompt: ``` You are a helpful assistant in recongnizes the content of tables in markdown format. Here is a table as fellows. You need to answer my question about the table.\n# Table\n|Opening|Opening|Sl. No.|Film|Cast|Director|Music Director|Notes|\n|----|----|----|----|----|----|----|----|\n|J A N|9|1|Agni Pushpam|Jayabharathi, Kamalahasan|Jeassy|M. K. Arjunan||\n|J A N|16|2|Priyamvada|Mohan Sharma, Lakshmi, KPAC Lalitha|K. S. Sethumadhavan|V. Dakshinamoorthy||\n|J A N|23|3|Yakshagaanam|Madhu, Sheela|Sheela|M. S. Viswanathan||\n|J A N|30|4|Paalkkadal|Sheela, Sharada|T. K. Prasad|A. T. Ummer||\n|F E B|5|5|Amma|Madhu, Srividya|M. Krishnan Nair|M. K. Arjunan||\n|F E B|13|6|Appooppan|Thikkurissi Sukumaran Nair, Kamal Haasan|P. Bhaskaran|M. S. Baburaj||\n|F E B|20|7|Srishti|Chowalloor Krishnankutty, Ravi Alu...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: er.running at once) I have set temperature=0 to obtain a fixed output. Model: llama-7b, prompt: ``` You are a helpful assistant in recongnizes the content of tables in markdown format. Here is a table as fellows. You ne...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: f without prefix will also affected when batchsize is too big(seems when requests can't be push into scheduler.running at once) I have set temperature=0 to obtain a fixed output. Model: llama-7b, prompt: ``` You are a h...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: shpam|Jayabharathi, Kamalahasan|Jeassy|M. K. Arjunan ``` My test script(imported from jupyter): ```python # %% # generate test prompt test_table = "|Opening|Opening|Sl. No.|Film|Cast|Director|Music Director|Notes|\n|---...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: save_file.name} {datetime.datetime.now()}") # %% # set gpus os.environ['CUDA_VISIBLE_DEVICES']="0" # init model and sampling parames tensor_parallel_size = len(os.getenv('CUDA_VISIBLE_DEVICES').split(',')) # set baichua...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 9|Samasya|Madhu, Kamalahaasan|K. Thankappan|Shyam||\n|F E B|27|10|Yudhabhoomi|K. P. Ummer, Vidhubala|Crossbelt Mani|R. K. Shekhar||\n|M A R|5|11|Seemantha Puthran|Prem Nazir, Jayabharathi|A. B. Raj|M. K. Arjunan||\n|M A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
