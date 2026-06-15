# vllm-project/vllm#32324: [Feature]: Support setting the default max_graph_size according to different platforms

| 字段 | 值 |
| --- | --- |
| Issue | [#32324](https://github.com/vllm-project/vllm/issues/32324) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support setting the default max_graph_size according to different platforms

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm working on deploying vLLM with wide-EP scenarios on Ascend NPU platform. While setting `num_speculative_tokens = 3` and `max_num_seqs=40`, the computed `max_cudagraph_capture_size` is 320 instead of 160 since following code in `vllm/config/vllm.py`: ``` if max_cudagraph_capture_size is None: decode_query_len = 1 if ( self.speculative_config and self.speculative_config.num_speculative_tokens ): decode_query_len += self.speculative_config.num_speculative_tokens max_cudagraph_capture_size = min( self.scheduler_config.max_num_seqs * decode_query_len * 2, 512 ) ``` I am curious about why we need to multiply `max_num_seqs * (1 + num_speculative_tokens)` by this magic number 2. This implementation leads to more and larger graph_capture_sizes and larger VRAM allocation on Asend NPU platform (except graph capturing cost with larger batch_size, `dispatch` and `combine` operators also allocate large buffer according to `max_cudagraph_capture_size`). I think this extra VRAM costs would not only occur in Ascend NPU, and this configuration does not provide any decoding performance benefits, except in extreme cases involving sporadic P‑requests with fe...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ting the default max_graph_size according to different platforms feature request;stale ### 🚀 The feature, motivation and pitch I'm working on deploying vLLM with wide-EP scenarios on Ascend NPU platform. While setting `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g `num_speculative_tokens = 3` and `max_num_seqs=40`, the computed `max_cudagraph_capture_size` is 320 instead of 160 since following code in `vllm/config/vllm.py`: ``` if max_cudagraph_capture_size is None: decode_quer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Asend NPU platform (except graph capturing cost with larger batch_size, `dispatch` and `combine` operators also allocate large buffer according to `max_cudagraph_capture_size`). I think this extra VRAM costs would not o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: agraph_capture_size` is 320 instead of 160 since following code in `vllm/config/vllm.py`: ``` if max_cudagraph_capture_size is None: decode_query_len = 1 if ( self.speculative_config and self.speculative_conf
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
