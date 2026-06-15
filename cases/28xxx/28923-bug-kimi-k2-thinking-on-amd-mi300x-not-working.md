# vllm-project/vllm#28923: [Bug]: kimi-k2-thinking on AMD MI300X not working

| 字段 | 值 |
| --- | --- |
| Issue | [#28923](https://github.com/vllm-project/vllm/issues/28923) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: kimi-k2-thinking on AMD MI300X not working

### Issue 正文摘录

### Your current environment Hi I am trying to deploy kimi-k2-thinking model on AMD MI300X but it is getting OOM killed in Kubernetes pod. I tried to allocate 1.5 Ti memory but still failed to load with `rocm/vllm-dev:nightly_main_20251117` container image. It is working fine with `rocm/vllm-dev:nightly_main_20251110` with `--enforce-eager`. but crashing after few requests without `--enforce-eager`. can you please help, suggest any work around. using below command to run. ``` python3 -m vllm.entrypoints.openai.api_server \ --port 8080 \ --served-model-name kimi-k2 \ --model /models/moonshotai/Kimi-K2-Thinking \ --trust-remote-code \ --enable-auto-tool-choice \ --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2 \ --max-model-len 100K \ --tensor-parallel-size 4 \ --enforce-eager \ --async-scheduling ``` ### 🐛 Describe the bug Hi I am trying to deploy kimi-k2-thinking model on AMD MI300X but it is getting OOM killed. I tried to allocate 1.5 Ti memory but still failed to load with `rocm/vllm-dev:nightly_main_20251117` docker image. It is working fine with `rocm/vllm-dev:nightly_main_20251110` with `--enforce-eager`. but crashing after few requests without `--enforce-eager`. can y...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: kimi-k2-thinking on AMD MI300X not working bug;rocm;stale ### Your current environment Hi I am trying to deploy kimi-k2-thinking model on AMD MI300X but it is getting OOM killed in Kubernetes pod. I tried to allo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: kimi-k2-thinking on AMD MI300X not working bug;rocm;stale ### Your current environment Hi I am trying to deploy kimi-k2-thinking model on AMD MI300X but it is getting OOM killed in Kubernetes pod. I tried to allo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: mory but still failed to load with `rocm/vllm-dev:nightly_main_20251117` docker image. It is working fine with `rocm/vllm-dev:nightly_main_20251110` with `--enforce-eager`. but crashing after few requests without `--enf...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: trying to deploy kimi-k2-thinking model on AMD MI300X but it is getting OOM killed in Kubernetes pod. I tried to allocate 1.5 Ti memory but still failed to load with `rocm/vllm-dev:nightly_main_20251117` container image...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ### Your current environment Hi I am trying to deploy kimi-k2-thinking model on AMD MI300X but it is getting OOM killed in Kubernetes pod. I tried to allocate 1.5 Ti memory but still failed to load with `rocm/vllm-dev:n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
