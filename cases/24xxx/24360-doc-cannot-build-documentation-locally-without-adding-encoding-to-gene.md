# vllm-project/vllm#24360: [Doc]: Cannot build documentation locally without adding encoding to generate examples

| 字段 | 值 |
| --- | --- |
| Issue | [#24360](https://github.com/vllm-project/vllm/issues/24360) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Cannot build documentation locally without adding encoding to generate examples

### Issue 正文摘录

### 📚 The doc issue `generate_examples` raises an error while building locally with the most recent `vllm` build To solve that ``` # Generate the example documentation for example in sorted(examples, key=lambda e: e.path.stem): example_name = f"{example.path.stem}.md" doc_path = EXAMPLE_DOC_DIR / example.category / example_name if not doc_path.parent.exists(): doc_path.parent.mkdir(parents=True) with open(doc_path, "w+", encoding="utf-8") as f: f.write(example.generate()) ``` and ``` def determine_title(self) -> str: if not self.is_code: with open(self.main_file, encoding="utf-8") as f: first_line = f.readline().strip() match = re.match(r'^#\s+(?P .+)$', first_line) if match: return match.group('title') return fix_case(self.path.stem.replace("_", " ").title()) ``` was necessary What is going on here with encoding? Should I add that to the docs themselves? Apprently if docs are being built properly I think this has to do with just my local then, is it? @hmellor ### Suggest a potential alternative/fix add UTF-8 to file read and writes. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corne...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Doc]: Cannot build documentation locally without adding encoding to generate examples documentation ### 📚 The doc issue `generate_examples` raises an error while building locally with the most recent `vllm` build To so...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
