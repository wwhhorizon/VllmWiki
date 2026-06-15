# vllm-project/vllm#25994: [Bug]: DeepSeek-V3.1 gives garbage output

| 字段 | 值 |
| --- | --- |
| Issue | [#25994](https://github.com/vllm-project/vllm/issues/25994) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V3.1 gives garbage output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am deploying DeepSeek-V3.1 in a 1p1d config with this yaml https://github.com/smarterclayton/ig-load/blob/v0.10.2/config/deploy_base_deepseek_r1_ep_pd.yaml on B200 with RDMA. My pods comes up successfully but when I send a prompt it returns garbage. How to reproduce: 1. Deploy https://github.com/smarterclayton/ig-load/blob/v0.10.2/config/deploy_base_deepseek_r1_ep_pd.yaml 2. Port-forward the decode pod: `kubectl port-forward pod/vllm-deepseek-r1-ep-pd-0 8200:8200` 3. Find the IP of the prefill pod `kubectl get pod/vllm-deepseek-r1-ep-pd-0-1 -o wide` 4. Send a prompt (make sure to replace ): ``` curl http://localhost:8200/v1/completions \ -H "Content-Type: application/json" \ -H "x-prefiller-host-port: http:// :8000" \ -d '{ "model": "deepseek-ai/DeepSeek-V3.1", "prompt": "Write as if you were a critic: San Francisco", "max_tokens": 70 }' {"id":"cmpl-44688b5f-9e44-11f0-bf1a-56b81a8db875","object":"text_completion","created":1759267720,"model":"deepseek-ai/DeepSeek-V3.1","choices":[{"index":0,"text":" a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ploying DeepSeek-V3.1 in a 1p1d config with this yaml https://github.com/smarterclayton/ig-load/blob/v0.10.2/config/deploy_base_deepseek_r1_ep_pd.yaml on B200 with RDMA. My pods comes up successfully but when I send a p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: DeepSeek-V3.1 gives garbage output bug;stale ### Your current environment ### 🐛 Describe the bug I am deploying DeepSeek-V3.1 in a 1p1d config with this yaml https://github.com/smarterclayton/ig-load/blob/v0.10.2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: eepSeek-V3.1", "prompt": "Write as if you were a critic: San Francisco", "max_tokens": 70 }' {"id":"cmpl-44688b5f-9e44-11f0-bf1a-56b81a8db875","object":"text_completion","created":1759267720,"model":"deepseek-ai/DeepSee...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nment ### 🐛 Describe the bug I am deploying DeepSeek-V3.1 in a 1p1d config with this yaml https://github.com/smarterclayton/ig-load/blob/v0.10.2/config/deploy_base_deepseek_r1_ep_pd.yaml on B200 with RDMA. My pods comes...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _support;moe;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
