# vllm-project/vllm#769: Offline compilation and installation error

| 字段 | 值 |
| --- | --- |
| Issue | [#769](https://github.com/vllm-project/vllm/issues/769) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Offline compilation and installation error

### Issue 正文摘录

When I installed vllm offline, I have already installed the 1.11.1 version of ninja, but when compiling and installing, I still need the network to download the ninja installation package Error: ![image](https://github.com/vllm-project/vllm/assets/49968353/c2d9456c-3af8-44ad-a603-f22426ec006d) ![image](https://github.com/vllm-project/vllm/assets/49968353/8468cfd5-651e-4471-ac31-ee350bacffa0) ![image](https://github.com/vllm-project/vllm/assets/49968353/63719e69-ef86-4154-8965-c64adb5c3022)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Offline compilation and installation error When I installed vllm offline, I have already installed the 1.11.1 version of ninja, but when compiling and installing, I still need the network to download the ninja installat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
