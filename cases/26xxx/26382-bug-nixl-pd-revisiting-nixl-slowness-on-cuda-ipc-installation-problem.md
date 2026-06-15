# vllm-project/vllm#26382: [Bug][NIXL][PD]: Revisiting NIXL slowness on CUDA_IPC -- installation problem

| 字段 | 值 |
| --- | --- |
| Issue | [#26382](https://github.com/vllm-project/vllm/issues/26382) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][NIXL][PD]: Revisiting NIXL slowness on CUDA_IPC -- installation problem

### Issue 正文摘录

Hi all, I wanted to follow up on a issue that I have sporadically fixed with help from @robertgshaw2-redhat , but not sure what the long term fix is. Happy to make PRs to get this issue out of the way, just need some agreement on what needs to be done. In [2025-07-03 NIXL Perf OH Runbook](https://docs.google.com/document/d/1c6zSg7xFkguqflx5jh-moRwCjoP4qNln8DE0mwNTjHk/edit?tab=t.0#heading=h.kyrfahp9yghe) @robertgshaw2-redhat points out a performance issue with NIXL having a transfer launch overhead and analyzes the implication of that overhead when using CUDA_IPC vs. IB. There is also a proposed fix for that issue which implies changes to both Nixl c++ layer, and changes to vLLM NIXL connector. I have separately validated that particular fix on a performance issue that I was seeing while serving gptoss-120B with P4TP1-D2TP2 on an 8xH100. My fixes follow the proposed fixes by Robert by stitching together a nixl and vllm patch as follows: 1. Install a custom branch of Nixl (from Rob’s [fork](https://github.com/robertgshaw2-redhat/nixl/tree/batched-workers)) ``` mkdir -p ~/default/patches && cd ~/default/patches git clone https://github.com/Pyngon/nixl.git cd nixl git remote add rober...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug][NIXL][PD]: Revisiting NIXL slowness on CUDA_IPC -- installation problem bug Hi all, I wanted to follow up on a issue that I have sporadically fixed with help from @robertgshaw2-redhat , but not sure what the long...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug][NIXL][PD]: Revisiting NIXL slowness on CUDA_IPC -- installation problem bug Hi all, I wanted to follow up on a issue that I have sporadically fixed with help from @robertgshaw2-redhat , but not sure what the long...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: s: [nixl_inc_dirs, ucx_utils_inc_dirs, '../../../../src/plugins/ucx'])|" test/unit/plugins/ucx/meson.build test/unit/plugins/ucx_mo/meson.build meson setup build --prefix=/usr/local/nixl/ -Ducx_path=/usr/local/ucx cd bu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 007-131635", "endpoint_type": "vllm", "backend": "vllm", "label": null, "model_id": "openai/gpt-oss-120b", "tokenizer_id": "openai/gpt-oss-120b", "num_prompts": 512, "request_rate": 8.0, "burstiness": 1.0, "max_concurre...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t do these replacements the installation of nixl will barf sed -i "s|ucx_backend_dep = declare_dependency(link_with: ucx_backend_lib, include_directories: \[nixl_inc_dirs, '../../../../src/plugins/ucx'\])|ucx_backend_de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
