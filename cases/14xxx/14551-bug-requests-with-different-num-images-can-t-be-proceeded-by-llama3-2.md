# vllm-project/vllm#14551: [Bug]: Requests with different num_images can't be proceeded by Llama3.2

| 字段 | 值 |
| --- | --- |
| Issue | [#14551](https://github.com/vllm-project/vllm/issues/14551) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Requests with different num_images can't be proceeded by Llama3.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug As mentioned in mllama.py [here](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mllama.py#L1224), ```python # tensor with the same shape will be batched together by # MultiModalKwargs.batch, so pixel_values here can be: # - List[List[torch.Tensor]]: # with shape (num_tiles, 3, image_res, image_res) # - List[torch.Tensor]: # with shape (num_image, num_tiles, 3, image_res, image_res) # - torch.Tensor: # with shape (bs, num_image, num_tiles, 3, image_res, image_res) ``` when requests with different num_image, same num_tiles, channel, image_res, image_res, the batched output will be List[torch.Tensor]. But when do the forward [here](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mllama.py#L662), we actually don't handle this case: ```python def forward(self, pixel_values: torch.Tensor, aspect_ratio_ids: torch.Tensor, aspect_ratio_mask: torch.Tensor) -> torch.Tensor: batch_size, num_concurrent_media, num_tiles, num_channels, \ height, width = pixel_values.shape ``` Does it mean that llama3.2 doesn't support requests with different num_images? ### Before submitting a new issue... -...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Requests with different num_images can't be proceeded by Llama3.2 bug ### Your current environment ### 🐛 Describe the bug As mentioned in mllama.py [here](https://github.com/vllm-project/vllm/blob/main/vllm/model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Requests with different num_images can't be proceeded by Llama3.2 bug ### Your current environment ### 🐛 Describe the bug As mentioned in mllama.py [here](https://github.com/vllm-project/vllm/blob/main/vllm/model...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
