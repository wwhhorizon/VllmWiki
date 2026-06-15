# vllm-project/vllm#19356: [Bug]: Key 'actor_rollout_ref' is not in struct when using async rollout server

| 字段 | 值 |
| --- | --- |
| Issue | [#19356](https://github.com/vllm-project/vllm/issues/19356) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Key 'actor_rollout_ref' is not in struct when using async rollout server

### Issue 正文摘录

### Your current environment Not included as it is not relevant to the bug recreate. ### 🐛 Describe the bug Updated to the latest veRL code of the main branch, enabling async rollout server with grpo training results to the following error: ``` Loading checkpoint shards: 100%|██████████| 4/4 [00:11 ) File "/workspace/src/verl/verl/trainer/main_ppo.py", line 177, in run trainer.init_workers() File "/workspace/src/verl/verl/trainer/ppo/ray_trainer.py", line 774, in init_workers self.async_rollout_manager = AsyncLLMServerManager( File "/workspace/src/verl/verl/workers/rollout/async_server.py", line 111, in __init__ self.config = config.actor_rollout_ref File "/root/miniconda3/envs/verl/lib/python3.10/site-packages/omegaconf/dictconfig.py", line 359, in __getattr__ self._format_and_raise(key=key, value=None, cause=e) File "/root/miniconda3/envs/verl/lib/python3.10/site-packages/omegaconf/base.py", line 231, in _format_and_raise format_and_raise( File "/root/miniconda3/envs/verl/lib/python3.10/site-packages/omegaconf/_utils.py", line 819, in format_and_raise _raise(ex, cause) File "/root/miniconda3/envs/verl/lib/python3.10/site-packages/omegaconf/_utils.py", line 797, in _raise raise e...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rl/verl/workers/rollout/async_server.py", line 111, in __init__ self.config = config.actor_rollout_ref File "/root/miniconda3/envs/verl/lib/python3.10/site-packages/omegaconf/dictconfig.py", line 359, in __getattr__ sel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lout.mode == "async": from verl.workers.rollout.async_server import AsyncLLMServerManager self.async_rollout_mode = True self.async_rollout_manager = AsyncLLMServerManager( config=self.config.actor_rollout_ref, worker_g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: relevant to the bug recreate. ### 🐛 Describe the bug Updated to the latest veRL code of the main branch, enabling async rollout server with grpo training results to the following error: ``` Loading checkpoint shards: 10...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
