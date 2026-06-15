# vllm-project/vllm#5723: [RFC]: Add runtime weight update API

| 字段 | 值 |
| --- | --- |
| Issue | [#5723](https://github.com/vllm-project/vllm/issues/5723) |
| 状态 | closed |
| 标签 | RFC;unstale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add runtime weight update API

### Issue 正文摘录

### Motivation. In online RL training, vLLM can significantly accelerate the rollout stage. To achieve this, we need weight sync from main training process to vLLM worker process, and then call the existing API in vLLM to update the weights by `model_runner.model.load_weights ` An example of such implementation can be found in OpenRLHF, [https://github.com/OpenLLMAI/OpenRLHF/blob/main/openrlhf/trainer/ray/vllm_worker_wrap.py](vllm_worker_wrap) However, user has to monkey patch vLLM worker to introduce such behavior. It would be great if vLLM naturally supports weight sync at runtime. ### Proposed Change. 1. Add a NCCL-based weight sync process group during vLLM initialization, so that main process can dist.broadcast weight to vLLM worker process later 2. Expose a weight sync API, for example: `def update_weight(self, name, dtype, shape)` then in master process, user can achieve weight sync via the following (modified from OpenRLHF): ``` for name, param in model.named_parameters(): # Fire all vllm engines for broadcast if torch.distributed.get_rank() == 0: shape = param.shape if self.strategy.args.zero_stage != 3 else param.ds_shape refs = [ engine.update_weight.remote(name, dtype=...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rocess, and then call the existing API in vLLM to update the weights by `model_runner.model.load_weights ` An example of such implementation can be found in OpenRLHF, [https://github.com/OpenLLMAI/OpenRLHF/blob/main/ope...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 2. Expose a weight sync API, for example: `def update_weight(self, name, dtype, shape)` then in master process, user can achieve weight sync via the following (modified from OpenRLHF): ``` for name, param in model.named...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: == 0: shape = param.shape if self.strategy.args.zero_stage != 3 else param.ds_shape refs = [ engine.update_weight.remote(name, dtype=param.dtype, shape=shape, empty_cache=count == num_params) for engine in self.vllm_eng...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Add runtime weight update API RFC;unstale ### Motivation. In online RL training, vLLM can significantly accelerate the rollout stage. To achieve this, we need weight sync from main training process to vLLM worker...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
