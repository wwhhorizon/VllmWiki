# vllm-project/vllm#6647: [Bug]: wheel size exceeds 200MB

| 字段 | 值 |
| --- | --- |
| Issue | [#6647](https://github.com/vllm-project/vllm/issues/6647) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: wheel size exceeds 200MB

### Issue 正文摘录

### Your current environment ```text - ``` ### 🐛 Describe the bug Seems like the main branch of vLLM is oversized, which is crashing the docker build process :/ ``` => ERROR [build 15/15] RUN python3 check-wheel-size.py dist 0.3s ------ > [build 15/15] RUN python3 check-wheel-size.py dist: 0.309 Wheel dist/vllm-0.5.2+cu124-cp38-abi3-linux_x86_64.whl is too large (204.7188196182251 MB) compare to the allowed size (200 MB). 0.309 vllm/_C.abi3.so: 282.28890228271484 MBs uncompressed. 0.309 vllm/_punica_C.abi3.so: 158.21475219726562 MBs uncompressed. 0.309 vllm/_moe_C.abi3.so: 13.828536987304688 MBs uncompressed. 0.309 vllm/config.py: 0.06867504119873047 MBs uncompressed. 0.309 vllm/worker/model_runner.py: 0.06034278869628906 MBs uncompressed. 0.309 vllm/core/scheduler.py: 0.05170249938964844 MBs uncompressed. 0.309 vllm/engine/llm_engine.py: 0.049073219299316406 MBs uncompressed. 0.309 vllm/lora/layers.py: 0.046690940856933594 MBs uncompressed. 0.309 vllm/model_executor/layers/sampler.py: 0.046222686767578125 MBs uncompressed. 0.309 vllm/spec_decode/spec_decode_worker.py: 0.040375709533691406 MBs uncompressed. ------ 3 warnings found (use --debug to expand): - FromAsCasing: 'as' and...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: wheel size exceeds 200MB bug ### Your current environment ```text - ``` ### 🐛 Describe the bug Seems like the main branch of vLLM is oversized, which is crashing the docker build process :/ ``` => ERROR [build 15...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 309 vllm/_moe_C.abi3.so: 13.828536987304688 MBs uncompressed. 0.309 vllm/config.py: 0.06867504119873047 MBs uncompressed. 0.309 vllm/worker/model_runner.py: 0.06034278869628906 MBs uncompressed. 0.309 vllm/core/schedule...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: r/model_runner.py: 0.06034278869628906 MBs uncompressed. 0.309 vllm/core/scheduler.py: 0.05170249938964844 MBs uncompressed. 0.309 vllm/engine/llm_engine.py: 0.049073219299316406 MBs uncompressed. 0.309 vllm/lora/layers...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: vllm/_punica_C.abi3.so: 158.21475219726562 MBs uncompressed. 0.309 vllm/_moe_C.abi3.so: 13.828536987304688 MBs uncompressed. 0.309 vllm/config.py: 0.06867504119873047 MBs uncompressed. 0.309 vllm/worker/model_runner.py:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
