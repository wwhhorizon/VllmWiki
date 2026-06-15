# vllm-project/vllm#27680: ☂️[AMD][CI Failure]: AMD CI Issues Master

| 字段 | 值 |
| --- | --- |
| Issue | [#27680](https://github.com/vllm-project/vllm/issues/27680) |
| 状态 | closed |
| 标签 | rocm;unstale;ci-failure |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention;cuda;triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ☂️[AMD][CI Failure]: AMD CI Issues Master

### Issue 正文摘录

Overall doc: https://docs.google.com/document/d/1rBtSQ7bbrzFbSX3IjULmqZtYVxpVgqEo_A9W0PytxiM/edit?tab=t.0#heading=h.bqg584n9zp0v CI tests migration status: https://docs.google.com/spreadsheets/d/1fSn5VvgOB_Zwm3zpbRqKQ3jrlSL_Dum9Ez5bz5agumE/edit?gid=0#gid=0 ### Umbrella Issue to track all AMD related CI failures #### Ongoing: ##### P0 (Fix V1 Tests, and add E2E tests): - [ ] https://github.com/vllm-project/vllm/issues/28320: - Added: Qwen3-235B, GPT-OSS, Llama4 Maverick - Pending: DeepSeek-R1 - [x] https://github.com/vllm-project/vllm/issues/29114 - [x] https://github.com/vllm-project/vllm/issues/29115 - [x] https://github.com/vllm-project/vllm/issues/29116 - [x] https://github.com/vllm-project/vllm/issues/27442: Attempting fix in https://github.com/vllm-project/vllm/pull/28346, https://github.com/vllm-project/vllm/pull/28156 ##### P1 (Fix Remaining Tests) - [x] https://github.com/vllm-project/vllm/issues/27442: Attempting fix in https://github.com/vllm-project/vllm/pull/28346, https://github.com/vllm-project/vllm/pull/28156 - [x] https://github.com/vllm-project/vllm/issues/27945 - [x] https://github.com/vllm-project/vllm/issues/28314 ...More issues WIP... #### Fixed Issues / Enabl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ): - [ ] https://github.com/vllm-project/vllm/issues/28320: - Added: Qwen3-235B, GPT-OSS, Llama4 Maverick - Pending: DeepSeek-R1 - [x] https://github.com/vllm-project/vllm/issues/29114 - [x] https://github.com/vllm-proj...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ☂️[AMD][CI Failure]: AMD CI Issues Master rocm;unstale;ci-failure Overall doc: https://docs.google.com/document/d/1rBtSQ7bbrzFbSX3IjULmqZtYVxpVgqEo_A9W0PytxiM/edit?tab=t.0#heading=h.bqg584n9zp0v CI tests migration statu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ☂️[AMD][CI Failure]: AMD CI Issues Master rocm;unstale;ci-failure Overall doc: https://docs.google.com/document/d/1rBtSQ7bbrzFbSX3IjULmqZtYVxpVgqEo_A9W0PytxiM/edit?tab=t.0#heading=h.bqg584n9zp0v CI tests migration statu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ☂️[AMD][CI Failure]: AMD CI Issues Master rocm;unstale;ci-failure Overall doc: https://docs.google.com/document/d/1rBtSQ7bbrzFbSX3IjULmqZtYVxpVgqEo_A9W0PytxiM/edit?tab=t.0#heading=h.bqg584n9zp0v CI tests migration statu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: - CPU KV on ROCm: https://github.com/vllm-project/vllm/pull/27770 - Make Triton attention usable with spec decode on CUDA/ROCm: https://github.com/vllm-project/vllm/pull/28432 - fastsafetensors on ROCm: https://github.c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
