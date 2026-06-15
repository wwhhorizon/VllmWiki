# vllm-project/vllm#3190: Unable to run distributed inference on ray with tensor parallel size > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#3190](https://github.com/vllm-project/vllm/issues/3190) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Unable to run distributed inference on ray with tensor parallel size > 1

### Issue 正文摘录

I am referring to https://github.com/vllm-project/vllm/blob/main/examples/offline_inference_distributed.py example. The suggestion in the example is not to set num_gpus when tensor parallel is used. However with that I ran into following issue: Ray does not allocate any GPUs on the driver node. Consider adjusting the Ray placement group or running the driver on a GPU node. I assume this is because the head node does not have GPUs configured. I then tried the ray placement group as recommended. Here is the code snippet for it: ``` resource_bundles = [{"GPU": 1, "CPU": 1} for i in range(8)] pg = placement_group(resource_bundles, strategy="PACK") ready, unready = ray.wait([pg.ready()], timeout=60) predictions = dataset.map_batches(VLLMPredictor,batch_format="numpy", batch_size=100, concurrency=4, scheduling_strategy=PlacementGroupSchedulingStrategy(placement_group=pg)) ``` With this however the job was stuck at loading model phase and eventually timed out. I then tried to set GPU to 2 in bundle as I have set tensor parallel size 2, but now I started getting following error: Placement group bundle cannot have more than 1 GPU. Is there a reason vLLM restricts GPU size to be just 1?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: n a GPU node. I assume this is because the head node does not have GPUs configured. I then tried the ray placement group as recommended. Here is the code snippet for it: ``` resource_bundles = [{"GPU": 1, "CPU": 1} for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
