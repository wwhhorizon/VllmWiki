# vllm-project/vllm#545: Slow installation:  install all versions of one package.

| 字段 | 值 |
| --- | --- |
| Issue | [#545](https://github.com/vllm-project/vllm/issues/545) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Slow installation:  install all versions of one package.

### Issue 正文摘录

I follow the document and it will install all versions of one package. ``` Downloading fonttools-4.24.0-py3-none-any.whl (853 kB) |████████████████████████████████| 853 kB 22.8 MB/s Downloading fonttools-4.23.1-py3-none-any.whl (853 kB) |████████████████████████████████| 853 kB 24.7 MB/s Downloading fonttools-4.23.0-py3-none-any.whl (852 kB) |████████████████████████████████| 852 kB 23.7 MB/s Downloading fonttools-4.22.1-py3-none-any.whl (850 kB) |████████████████████████████████| 850 kB 70.3 MB/s Downloading fonttools-4.22.0-py3-none-any.whl (850 kB) |████████████████████████████████| 850 kB 45.1 MB/s INFO: pip is looking at multiple versions of cycler to determine which version is compatible with other requirements. This could take a while. Collecting cycler>=0.10 ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Slow installation: install all versions of one package. I follow the document and it will install all versions of one package. ``` Downloading fonttools-4.24.0-py3-none-any.whl (853 kB) |██████████████████████████████

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
