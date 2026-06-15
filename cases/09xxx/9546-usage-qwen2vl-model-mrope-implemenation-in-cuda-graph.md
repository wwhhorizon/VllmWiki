# vllm-project/vllm#9546: [Usage]: Qwen2VL model mrope implemenation in cuda graph 

| 字段 | 值 |
| --- | --- |
| Issue | [#9546](https://github.com/vllm-project/vllm/issues/9546) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;multimodal_vlm |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Qwen2VL model mrope implemenation in cuda graph 

### Issue 正文摘录

### Anything you want to discuss about vllm. in qwen2vl's mrope imple, vllm decide whether input positions is for multimodal with ![image](https://github.com/user-attachments/assets/6dfc96d9-5162-4fbf-8759-031de22405e0) in RUNTIME. So, when input is text-only, the input positions is (seqlen). however, vllm's cuda graph use positions shape == (3, seqlen). ![image](https://github.com/user-attachments/assets/8d96aff4-a931-4804-9879-64ad1666544b) Does that means we can not use cuda graph for qwen2vl with text-only input. Otherwise, we get (seqlen) positions shape, but cuda graph deal with it as (3, seqlen)? However I do some tests, It seems no difference of final results between cuda graph and eager mode with text-only input? So I was wondering why. PS. I use nsys to profile the whole process, cuda-graph DO have two more kernels than eager mode. Left is cuda-graph, right is eager. ![image](https://github.com/user-attachments/assets/ddfb1034-2877-4c69-b2cf-846da3463a3e) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Qwen2VL model mrope implemenation in cuda graph stale ### Anything you want to discuss about vllm. in qwen2vl's mrope imple, vllm decide whether input positions is for multimodal with ![image](https://github.co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Qwen2VL model mrope implemenation in cuda graph stale ### Anything you want to discuss about vllm. in qwen2vl's mrope imple, vllm decide whether input positions is for multimodal with ![image](https://github.co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s shape, but cuda graph deal with it as (3, seqlen)? However I do some tests, It seems no difference of final results between cuda graph and eager mode with text-only input? So I was wondering why. PS. I use nsys to pro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ything you want to discuss about vllm. in qwen2vl's mrope imple, vllm decide whether input positions is for multimodal with ![image](https://github.com/user-attachments/assets/6dfc96d9-5162-4fbf-8759-031de22405e0) in RU...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Qwen2VL model mrope implemenation in cuda graph stale ### Anything you want to discuss about vllm. in qwen2vl's mrope imple, vllm decide whether input positions is for multimodal with ![image](https://github.co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
