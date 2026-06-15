# vllm-project/vllm#5304: installing build dependencies...|

| 字段 | 值 |
| --- | --- |
| Issue | [#5304](https://github.com/vllm-project/vllm/issues/5304) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> installing build dependencies...\|

### Issue 正文摘录

### Your current environment I use git clone to download new version of vllm，But it keeps getting stuck on Installing build dependencies ... - ### How you are installing vllm git clone https://github.com/vllm-project/vllm.git cd vllm # export VLLM_INSTALL_PUNICA_KERNELS=1 # optionally build for multi-LoRA capability pip install -e .

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: installing build dependencies...| installation ### Your current environment I use git clone to download new version of vllm，But it keeps getting stuck on Installing build dependencies ... - ### How you are installing v
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: # export VLLM_INSTALL_PUNICA_KERNELS=1 # optionally build for multi-LoRA capability pip install -e .

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
