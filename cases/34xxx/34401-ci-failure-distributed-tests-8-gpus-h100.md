# vllm-project/vllm#34401: [CI Failure]: Distributed Tests (8 GPUs)(H100)

| 字段 | 值 |
| --- | --- |
| Issue | [#34401](https://github.com/vllm-project/vllm/issues/34401) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Distributed Tests (8 GPUs)(H100)

### Issue 正文摘录

### Name of failing test torchrun --nproc-per-node=8 ../examples/offline_inference/torchrun_dp_example.py --tp-size=2 --pp-size=1 --dp-size=4 --enable-ep ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/51205/steps/canvas?jid=019c4ed0-0d32-485a-86d7-3480552709fe ``` [rank0]: Traceback (most recent call last): -- [rank0]: File "/vllm-workspace/tests/../examples/offline_inference/torchrun_dp_example.py", line 98, in [rank0]: llm = LLM( [rank0]: ^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/llm.py", line 346, in __init__ [rank0]: self.llm_engine = LLMEngine.from_engine_args( [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/llm_engine.py", line 174, in from_engine_args [rank0]: return cls( [rank0]: ^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/llm_engine.py", line 108, in __init__ [rank0]: self.engine_core = EngineCoreClient.make_client( [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: Distributed Tests (8 GPUs)(H100) ci-failure ### Name of failing test torchrun --nproc-per-node=8 ../examples/offline_inference/torchrun_dp_example.py --tp-size=2 --pp-size=1 --dp-size=4 --enable-ep ### Bas
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _example.py --tp-size=2 --pp-size=1 --dp-size=4 --enable-ep ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: Distributed Tests (8 GPUs)(H100) ci-failure ### Name of failing test torchrun --nproc-per-node=8 ../examples/offline_inference/torchrun_dp_example.py --tp-size=2 --pp-size=1 --dp-size=4 --enable-ep ### Bas...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: mpile.py", line 239, in aot_compile_fullgraph [rank0]: compiled_fn = backend( [rank0]: ^^^^^^^^ [rank0]: File "/usr/local/lib/python3.12/dist-packages/torch/__init__.py", line 2509, in __call__ [rank0]: return self.comp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: Distributed Tests (8 GPUs)(H100) ci-failure ### Name of failing test torchrun --nproc-per-node=8 ../examples/offline_inference/torchrun_dp_example.py --tp-size=2 --pp-size=1 --dp-size=4 --enable-ep ### Bas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
