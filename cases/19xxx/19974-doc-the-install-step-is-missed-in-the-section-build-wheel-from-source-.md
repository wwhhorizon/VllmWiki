# vllm-project/vllm#19974: [Doc]: The install step is missed in the section “Build wheel from source” in the Installation of CPU.

| 字段 | 值 |
| --- | --- |
| Issue | [#19974](https://github.com/vllm-project/vllm/issues/19974) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: The install step is missed in the section “Build wheel from source” in the Installation of CPU.

### Issue 正文摘录

### 📚 The doc issue Compared to v0.8.5, the installation step is missing in the "Build wheel from source" section under CPU Installation in v0.9.1 at: https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html ​​v0.9.1 page:​ ![Image](https://github.com/user-attachments/assets/8f118efc-67a8-4907-9af0-836ceba12f81) ​​v0.8.5 page:​​ ![Image](https://github.com/user-attachments/assets/0312d1fc-cbd0-46e4-874c-b1f22d1d7c15) As clearly visible in the screenshots, the specific installation steps have been removed, leaving users unable to follow the documented procedure. ### Suggest a potential alternative/fix Restore the installation steps similar to v0.8.5 in the "Build wheel from source" section. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Doc]: The install step is missed in the section “Build wheel from source” in the Installation of CPU. documentation ### 📚 The doc issue Compared to v0.8.5, the installation step is missing in the "Build wheel from sour...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: " section under CPU Installation in v0.9.1 at: https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html ​​v0.9.1 page:​ ![Image](https://github.com/user-attachments/assets/8f118efc-67a8-4907-9af0-836ceba12f8...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
