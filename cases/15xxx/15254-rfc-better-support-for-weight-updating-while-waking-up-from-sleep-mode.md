# vllm-project/vllm#15254: [RFC]: Better support for weight updating while waking up from sleep mode for RLHF

| 字段 | 值 |
| --- | --- |
| Issue | [#15254](https://github.com/vllm-project/vllm/issues/15254) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Better support for weight updating while waking up from sleep mode for RLHF

### Issue 正文摘录

### Motivation. Currently, when using sleep mode and wake_up() for RLHF, like in [verl](https://github.com/volcengine/verl/tree/main), we can run into issues like [here](https://github.com/volcengine/verl/issues/302), where we run into OOMs when waking up the vllm engine due to additional copies of the model living on the same GPU. The issue in verl specifically lives in the [fsdp_vllm sharding manager](https://github.com/volcengine/verl/blob/main/verl/workers/sharding_manager/fsdp_vllm.py#L94), where when we want to update weights for the woken up vllm engine, we have memory allocated for the old discarded weights, discarded kv cache, as well as the new copy of the weights all on the same gpu. A simplified version of this code is shown below, as well as a diagram demonstrating how OOM happens. ```python params = self.fsdp_module.state_dict() # new weights on GPU self.inference_engine.wake_up() # old weights + kv_cache memory allocated -> this can cause OOM for big models! self.inference_engine.llm_engine.model_executor.driver_worker.worker.model_runner.model.load_weights([(name, param) for name, param in params.items())]) ``` One thing here to note is that technically these issue...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [here](https://github.com/volcengine/verl/issues/302), where we run into OOMs when waking up the vllm engine due to additional copies of the model living on the same GPU. The issue in verl specifically lives in the [fsd...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tional copies of the model living on the same GPU. The issue in verl specifically lives in the [fsdp_vllm sharding manager](https://github.com/volcengine/verl/blob/main/verl/workers/sharding_manager/fsdp_vllm.py#L94), w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: en2.5-32B" train_model = AutoModelForCausalLM.from_pretrained(model).to("cuda") llm = LLM(model, enable_sleep_mode=True) llm.sleep(level=2) new_weights = train(train_model).state_dict() # train does some gradient update...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Better support for weight updating while waking up from sleep mode for RLHF RFC;stale ### Motivation. Currently, when using sleep mode and wake_up() for RLHF, like in [verl](https://github.com/volcengine/verl/tree/main)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: support for weight updating while waking up from sleep mode for RLHF RFC;stale ### Motivation. Currently, when using sleep mode and wake_up() for RLHF, like in [verl](https://github.com/volcengine/verl/tree/main), we ca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
