# vllm-project/vllm#39378: [Bug]: 0.19.0  rocm+7900xtx： Failed to infer device type

| 字段 | 值 |
| --- | --- |
| Issue | [#39378](https://github.com/vllm-project/vllm/issues/39378) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.19.0  rocm+7900xtx： Failed to infer device type

### Issue 正文摘录

### Your current environment vLLM：0.19.0 rocm：7.2 ### 🐛 Describe the bug (base) root@kittyzero:~# dpkg -l|grep rocm ii rocm 7.2.1.70201-81~24.04 amd64 Radeon Open Compute (ROCm) software stack meta package ii rocm-cmake 0.14.0.70201-81~24.04 amd64 rocm-cmake built using CMake ii rocm-core 7.2.1.70201-81~24.04 amd64 ROCm Runtime software stack ii rocm-dbgapi 0.77.4.70201-81~24.04 amd64 Library to provide AMD GPU debugger API ii rocm-debug-agent 2.1.0.70201-81~24.04 amd64 Radeon Open Compute Debug Agent (ROCdebug-agent) ii rocm-developer-tools 7.2.1.70201-81~24.04 amd64 Radeon Open Compute (ROCm) Runtime software stack ii rocm-device-libs 1.0.0.70201-81~24.04 amd64 Radeon Open Compute - device libraries ii rocm-gdb 16.3.70201-81~24.04 amd64 ROCgdb ii rocm-hip 7.2.1.70201-81~24.04 amd64 Radeon Open Compute (ROCm) Runtime software stack ii rocm-llvm 22.0.0.26084.70201-81~24.04 amd64 ROCm core compiler ii rocm-opencl 2.0.0.70201-81~24.04 amd64 clr built using CMake ii rocm-opencl-dev 2.0.0.70201-81~24.04 amd64 clr built using CMake ii rocm-opencl-sdk 7.2.1.70201-81~24.04 amd64 Radeon Open Compute (ROCm) Runtime software stack ii rocm-openmp 7.2.1.70201-81~24.04 amd64 Radeon Open Comput...

## 现有链接修复摘要

#41585 [ROCm] Fix platform detection failures in unprivileged containers

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 4 Radeon Open Compute (ROCm) software stack meta package ii rocm-cmake 0.14.0.70201-81~24.04 amd64 rocm-cmake built using CMake ii rocm-core 7.2.1.70201-81~24.04
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: 0.19.0 rocm+7900xtx： Failed to infer device type bug;rocm ### Your current environment vLLM：0.19.0 rocm：7.2 ### 🐛 Describe the bug (base) root@kittyzero:~# dpkg -l|grep rocm ii rocm
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ) root@kittyzero:~# python -m vllm.entrypoints.openai.api_server \ > --model Qwen/Qwen3.5-9B-Instruct-AWQ \ > --quantization awq \ > --gpu-memory-utilization 0.85 \ > --max-model-len 22000 \ > --enable-auto-tool-choice...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nts.openai.api_server \ > --model Qwen/Qwen3.5-9B-Instruct-AWQ \ > --quantization awq \ > --gpu-memory-utilization 0.85 \ > --max-model-len 22000 \ > --enable-auto-tool-choice \ > --tool-call-parser hermes Traceback (mo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;frontend_api;hardware_porting;model_support;quantization quantiz...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41585](https://github.com/vllm-project/vllm/pull/41585) | mentioned | 0.6 | [ROCm] Fix platform detection failures in unprivileged containers | tted when amdsmi fails Related issues: #40081, #24576, #34573, #39378 🤖 Generated with [Claude Code](https://claude.ai/code) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
