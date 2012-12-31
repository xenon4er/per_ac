/* Author:
km
*/

$(function () {
  tax_data = [
       {"period": "2012",  "sorned": 467},
       {"period": "2011 ",  "sorned": 646},
       {"period": "2010",  "sorned":323},
       {"period": "2009",  "sorned": 245},
       {"period": "2008",  "sorned": 654}
  ];
  new Morris.Line({
    element: 'hero-graph',
    data: tax_data,
    xkey: 'period',
    ykeys: ['sorned'],
    labels: ['$']
  });
  $('.code-example').each(function (index, el) {
    eval($(el).text());
  });
});
