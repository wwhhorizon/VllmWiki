# vllm-project/vllm#7540: [Performance]: Why does VLLM perform worse than TGI in Speculative decoding?

| 字段 | 值 |
| --- | --- |
| Issue | [#7540](https://github.com/vllm-project/vllm/issues/7540) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Why does VLLM perform worse than TGI in Speculative decoding?

### Issue 正文摘录

### Proposal to improve performance Hello Teacher, it is a great honor to witness your magnificent work. The team I am part of is currently trying to migrate the inference service from TGI to vLLM. However, we have encountered some issues in the effectiveness evaluation and hope that the teachers can provide guidance. question： 1、Could you please explain why the GPU utilization of vLLM is lower than that of TGI? Is it possible to increase the GPU utilization by adjusting parameters? 2、Why is the QPS of vLLM lower than that of TGI? How should this be considered and optimized? ### Report of performance regression Experimental DataScenario: In the agent scenario, the number of prompt tokens is between 30-40, and the number of output tokens is between 10-20. We have trained a small n-gram model as a draft model (with an accuracy rate of 70% when predicting num_speculative_tokens=4). We used 2,000 different data entries for stress testing. 🚀vLLM Startup Parameters: python3 vllm/entrypoints/openai/api_server.py \ --served-model-name base_model \ --port XXX \ --model XX \ --max_model_len 1000 \ --speculative_model="[ngram_pool]" \ --num_speculative_tokens 4 \ --use_v2_block_manager \ QPS...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: /assets/cb747057-6e56-462d-a121-e2561d3cb55f) 🚗TGI Startup Parameters: docker run -it --gpus=device=2 --network host \ --model-id model_path \ --num-shard 1 --port xxx --router-name=xx --max-top-n-tokens=1 --max-input-l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: -40, and the number of output tokens is between 10-20. We have trained a small n-gram model as a draft model (with an accuracy rate of 70% when predicting num_speculative_tokens=4). We used 2,000 different data entries...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Performance]: Why does VLLM perform worse than TGI in Speculative decoding? performance;stale ### Proposal to improve performance Hello Teacher, it is a great honor to witness your magnificent work. The team I am part...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: number of output tokens is between 10-20. We have trained a small n-gram model as a draft model (with an accuracy rate of 70% when predicting num_speculative_tokens=4). We used 2,000 different data entries for stress te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: I to vLLM. However, we have encountered some issues in the effectiveness evaluation and hope that the teachers can provide guidance. question： 1、Could you please explain why the GPU utilization of vLLM is lower than tha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
