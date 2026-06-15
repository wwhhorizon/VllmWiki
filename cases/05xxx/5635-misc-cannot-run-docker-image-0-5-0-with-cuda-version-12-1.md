# vllm-project/vllm#5635: [Misc]: cannot run docker image 0.5.0 with cuda version == 12.1

| 字段 | 值 |
| --- | --- |
| Issue | [#5635](https://github.com/vllm-project/vllm/issues/5635) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: cannot run docker image 0.5.0 with cuda version == 12.1

### Issue 正文摘录

### Anything you want to discuss about vllm. I have ubuntu-22.04, cuda==12.1, nvidia driver == 530, gpu==V100 when running newer version of vllm (after 0.4.3) , it does not work. According to the doc, vllm is built with cuda 12.1, so I think it should not require cuda>=12.4. Error log ``` docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error running hook #0: error running hook: exit status 1, stdout: , stderr: Auto-detected mode as 'legacy' nvidia-container-cli: requirement error: unsatisfied condition: cuda>=12.4, please update your driver to a newer version, or use an earlier cuda container: unknown. ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Misc]: cannot run docker image 0.5.0 with cuda version == 12.1 ### Anything you want to discuss about vllm. I have ubuntu-22.04, cuda==12.1, nvidia driver == 530, gpu==V100 when running newer version of vllm (after 0.4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Misc]: cannot run docker image 0.5.0 with cuda version == 12.1 ### Anything you want to discuss about vllm. I have ubuntu-22.04, cuda==12.1, nvidia driver == 530, gpu==V100 when running newer version of vllm (after 0.4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
