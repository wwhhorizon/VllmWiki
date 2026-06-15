# vllm-project/vllm#13662: [Feature]: Can it support avx cpu's like xeon E5-2670v2

| 字段 | 值 |
| --- | --- |
| Issue | [#13662](https://github.com/vllm-project/vllm/issues/13662) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Can it support avx cpu's like xeon E5-2670v2

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [Hardware][Intel] Support CPU inference with AVX2 ISA [#5452](https://github.com/vllm-project/vllm/pull/5452) In issue #5452, the expert DamonFool has implemented the ability to run vllm on CPUs with the AVX2 instruction set. However, my machine is an older Xeon E5-2670v2, which only supports AVX. Could anyone help modify the code to make it compatible with AVX? Thank you! 4.499 running build_ext 5.040 -- The CXX compiler identification is GNU 12.3.0 5.067 -- Detecting CXX compiler ABI info 5.270 -- Detecting CXX compiler ABI info - done 5.309 -- Check for working CXX compiler: /usr/bin/c++ - skipped 5.310 -- Detecting CXX compile features 5.311 -- Detecting CXX compile features - done 5.368 -- Build type: RelWithDebInfo 5.368 -- Target device: cpu 5.672 -- Found Python: /usr/bin/python3 (found version "3.10.12") found components: Interpreter Development.Module Development.SABIModule 5.672 -- Found python matching: /usr/bin/python3. 8.417 CMake Warning at /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message): 8.417 static library kineto_LIBRARY-NOTFOUND not found. 8.417 Call Stack (most recent call fi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: odify the code to make it compatible with AVX? Thank you! 4.499 running build_ext 5.040 -- The CXX compiler identification is GNU 12.3.0 5.067 -- Detecting CXX compiler ABI info 5.270 -- Detecting CXX compiler ABI info...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Can it support avx cpu's like xeon E5-2670v2 feature request;stale ### 🚀 The feature, motivation and pitch [Hardware][Intel] Support CPU inference with AVX2 ISA [#5452](https://github.com/vllm-project/vllm/pu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ake Warning at cmake/cpu_extension.cmake:133 (message): 8.441 vLLM CPU backend requires AVX512, AVX2, Power9+ ISA or ARMv8 support. 8.441 Call Stack (most recent call first): 8.441 CMakeLists.txt:89 (include) 8.441 8.44...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: supported for the current implementation. 46.75 9 | static_assert(false, "AVX2 must be supported for the current implementation."); 46.75 | ^~~~~ ### Alternatives _No response_ ### Additional context _No response_ ### B...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
