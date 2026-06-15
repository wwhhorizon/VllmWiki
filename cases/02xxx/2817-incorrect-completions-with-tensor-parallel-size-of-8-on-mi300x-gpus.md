# vllm-project/vllm#2817: Incorrect completions with tensor parallel size of 8 on MI300X GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#2817](https://github.com/vllm-project/vllm/issues/2817) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Incorrect completions with tensor parallel size of 8 on MI300X GPUs

### Issue 正文摘录

I'm encountering an issue where vLLM fails to generate complete or sensible responses when the tensor parallel size is set to 8 on MI300X GPUs. Completions work as expected with tensor parallel sizes of 1 and 4. **Expected behavior:** vLLM should generate a correct and meaningful completion for the given prompt, similar to its behavior with tensor parallel sizes of 1 and 4. **Actual behavior:** vLLM provides an incomplete or nonsensical response, often similar to the following: ```json "choices": [ { "index": 0, "message": { "role": "assistant", "content": " Installed-Size: 13.3 kB Depends: hipblas (= 2.0.0.60000-91~20.04), hipblaslt (= 0.6.0.60000-91~20.04), hipfft (= 1.0.12.60000-91~20.04), hipsolver (= 2.0.0.60000-91~20.04), hipsparse (= 3.0.0.60000-91~20.04), hiptensor (= 1.1.0.60000-91~20.04), miopen-hip (= 3.00.0.60000-91~20.04), half (= 1.12.0.60000-91~20.04), rccl (= 2.18.3.60000-91~20.04), rocalution (= 3.0.3.60000-91~20.04), rocblas (= 4.0.0.60000-91~20.04), rocfft (= 1.0.23.60000-91~20.04), rocrand (= 2.10.17.60000-91~20.04), hiprand (= 2.10.16.60000-91~20.04), rocsolver (= 3.24.0.60000-91~20.04), rocsparse (= 3.0.2.60000-91~20.04), rocm-core (= 6.0.0.60000-91~20.04), c...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Incorrect completions with tensor parallel size of 8 on MI300X GPUs rocm I'm encountering an issue where vLLM fails to generate complete or sensible responses when the tensor parallel size is set to 8 on MI300X GPUs. Co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ": { "role": "assistant", "content": " Installed-Size: 13.3 kB Depends: hipblas (= 2.0.0.60000-91~20.04), hipblaslt (= 0.6.0.60000-91~20.04), hipfft (= 1.0.12.60000-91~20.04), hipsolver (= 2.0.0.60000-91~20.04), hipspar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
