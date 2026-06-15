# vllm-project/vllm#40443: [BUG] Port-allocation race between ApiServer processes in hybrid-LB mode (ZMQError: Address already in use)

| 字段 | 值 |
| --- | --- |
| Issue | [#40443](https://github.com/vllm-project/vllm/issues/40443) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;moe;multimodal_vlm;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel;moe |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [BUG] Port-allocation race between ApiServer processes in hybrid-LB mode (ZMQError: Address already in use)

### Issue 正文摘录

## Summary Multi-node hybrid-LB deployments (DP > 1 across 2+ nodes, default `api_server_count`) intermittently fail during ApiServer startup with: ``` (ApiServer_N pid=...) zmq.error.ZMQError: Address already in use (addr='tcp:// : ') ... RuntimeError: Process ApiServer_N (PID: ...) died with exit code 1 RuntimeError: Engine core initialization failed. See root cause above. ``` Happens after weights/compile finish, before `Application startup complete`. Observed consistently on MoE / multimodal models (`Qwen3-30B-A3B-Instruct-2507`, `gpt-oss-120b`, `gemma-4-31B-it`) across 2n and 4n jobs; not observed on single-node or on small dense models. ## Minimal reproduction (no GPUs, no multi-node) Run anywhere vLLM is installed: ```python from vllm.v1.utils import get_engine_client_zmq_addr def probe_once(n_addrs: int) -> bool: addrs = [ get_engine_client_zmq_addr(local_only=False, host="127.0.0.1") for _ in range(n_addrs) ] return len(set(addrs)) dup trials: {dup}/{trials} ({100*dup/trials:.1f}%)") ``` On my box: ``` n= 8 -> dup trials: 0/1000 (0.0%) n= 16 -> dup trials: 8/1000 (0.8%) n= 32 -> dup trials: 38/1000 (3.8%) ``` `get_engine_zmq_addresses` calls `get_engine_client_zmq_addr` `...

## 现有链接修复摘要

#40596 [Bugfix] Close ApiServer ZMQ bind race with wildcard bind + pipe-back

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: initialization failed. See root cause above. ``` Happens after weights/compile finish, before `Application startup complete`. Observed consistently on MoE / multimodal models (`Qwen3-30B-A3B-Instruct-2507`, `gpt-oss-120...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: h, before `Application startup complete`. Observed consistently on MoE / multimodal models (`Qwen3-30B-A3B-Instruct-2507`, `gpt-oss-120b`, `gemma-4-31B-it`) across 2n and 4n jobs; not observed on single-node or on small...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: finish, before `Application startup complete`. Observed consistently on MoE / multimodal models (`Qwen3-30B-A3B-Instruct-2507`, `gpt-oss-120b`, `gemma-4-31B-it`) across 2n and 4n jobs; not observed on single-node or on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: emma-4-31B-it`) across 2n and 4n jobs; not observed on single-node or on small dense models. ## Minimal reproduction (no GPUs, no multi-node) Run anywhere vLLM is installed: ```python from vllm.v1.utils import get_engin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: # after (atomic) sock.bind(f"tcp://{host}:*") addr = sock.last_endpoint.decode() ``` Happy to put up a PR if this approach looks right. performance ci_build;distributed_parallel;frontend_api;moe;multimodal_vlm;scheduler...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40596](https://github.com/vllm-project/vllm/pull/40596) | closes_keyword | 0.95 | [Bugfix] Close ApiServer ZMQ bind race with wildcard bind + pipe-back | Resolves #40443. ## Approach Let each ApiServer child bind wildcard `tcp://host:0` so the kernel atomically assigns a port that the socket immediately owns — no window. Actual en |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
