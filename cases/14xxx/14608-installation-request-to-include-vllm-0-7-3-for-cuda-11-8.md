# vllm-project/vllm#14608: [Installation]: Request to include vllm==0.7.3 for cuda 11.8

| 字段 | 值 |
| --- | --- |
| Issue | [#14608](https://github.com/vllm-project/vllm/issues/14608) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Request to include vllm==0.7.3 for cuda 11.8

### Issue 正文摘录

### Your current environment I have a notebook using cuda 11.6 and nvidia Driver Version: 510.108.03. Python 3.10 or more This nvidia drivers are not compatible with cuda 12+. I can't update nvidia drivers or cuda in this jupyter notebook. I was able to install vllm 0.5.5 with cuda 11.8 and all will work fine. `pip install https://github.com/vllm-project/vllm/releases/download/v0.5.5/vllm-0.5.5+cu118-cp310-cp310-manylinux1_x86_64.wh` But if I will install `vllm==0.7.3` This installation will install cuda 12 and all will not work anymore due to mismatch between old nvidia drivers and cuda. I would like to know if vllm==0.7.3+cu118 will be added, or also for old versions or if vllm (from version 0.6.x) it's compatible only with cuda 12. Thanks ### How you are installing vllm ```sh pip install vllm==0.7.3 ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Request to include vllm==0.7.3 for cuda 11.8 installation ### Your current environment I have a notebook using cuda 11.6 and nvidia Driver Version: 510.108.03. Python 3.10 or more This nvidia drivers are
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: Request to include vllm==0.7.3 for cuda 11.8 installation ### Your current environment I have a notebook using cuda 11.6 and nvidia Driver Version: 510.108.03. Python 3.10 or more This nvidia drivers are...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s installation will install cuda 12 and all will not work anymore due to mismatch between old nvidia drivers and cuda. I would like to know if vllm==0.7.3+cu118 will be added, or also for old versions or if vllm (from v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: Request to include vllm==0.7.3 for cuda 11.8 installation ### Your current environment I have a notebook using cuda 11.6 and nvidia Driver Version: 510.108.03. Python 3.10 or more This nvidia drivers are...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
